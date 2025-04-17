import json
import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import sys
import argparse

def flatten_json(nested_json, parent_key='', sep='_'):
    """Recursively flattens a nested JSON object, including simple fields."""
    items = {}
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        # Adjust key truncation logic
        if ':' in new_key:
            new_key = new_key.split(':', 1)[1] if '_' not in new_key else new_key.rsplit('_', 1)[-1]
        if '$' in new_key:
            new_key = new_key.replace('$', '')
        if isinstance(v, dict):
            # Recursively flatten nested dictionaries
            nested_items = flatten_json(v, new_key, sep=sep)
            items.update(nested_items)
        elif isinstance(v, list):
            # Flatten lists by enumerating their items
            for i, item in enumerate(v):
                list_items = flatten_json({f"{new_key}_{i}": item}, '', sep=sep)
                items.update(list_items)
        else:
            # Add simple fields directly
            if new_key in items:
                print(f"Warning: Key collision detected for {new_key}. Overwriting value.")
            items[new_key] = v
    return items

def infer_column_types(data):
    """Infers PostgreSQL column types based on the data."""
    column_types = {}
    for row in data:
        for key, value in row.items():
            if value is None:
                continue
            if isinstance(value, bool):
                column_types[key] = "BOOLEAN"
            elif isinstance(value, int):
                column_types[key] = "INTEGER"
            elif isinstance(value, float):
                column_types[key] = "FLOAT"
            else:
                column_types[key] = "TEXT"
    return column_types

def load_to_postgres(data, table_name, connection_string, dry_run=False):
    """Loads data into a PostgreSQL table or prints SQL in dry-run mode."""
    # Convert data to a DataFrame
    df = pd.DataFrame(data)

    # Infer column types
    column_types = infer_column_types(data)

    # Create table SQL
    columns = ', '.join([f"{col} {column_types.get(col, 'TEXT')}" for col in df.columns])
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"

    # Insert data SQL
    insert_query_template = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES "
    values = df.values.tolist()

    if dry_run:
        # Print SQL statements
        print("-- Dry Run: SQL Statements")
        print(create_table_query)
        for row in values:
            # Construct the full INSERT statement for each row
            row_values = ', '.join(map(lambda x: f"'{x}'" if isinstance(x, str) else str(x), row))
            print(f"{insert_query_template}({row_values});")
    else:
        # Connect to PostgreSQL
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()

        # Execute create table
        cursor.execute(create_table_query)

        # Execute insert data
        insert_query = f"{insert_query_template} %s"
        execute_values(cursor, insert_query, values)

        # Commit and close
        conn.commit()
        cursor.close()
        conn.close()

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Flatten nested JSON and load into PostgreSQL.")
    parser.add_argument("table_name", help="Name of the PostgreSQL table to load data into.")
    parser.add_argument("--dry-run", action="store_true", help="Print SQL statements without executing them.")
    args = parser.parse_args()

    # Read JSON from STDIN
    data = json.load(sys.stdin)

    # Flatten the JSON data
    #flattened_data = [flatten_json(item) for item in data]
    flattened_data = []
    for item in data:
        vessels = item.get("vessels", {})
        for vessel_id, vessel_data in vessels.items():
            # Add the vessel ID as a prefix to ensure uniqueness
            flattened_vessel = flatten_json(vessel_data, parent_key=vessel_id)
            flattened_data.append(flattened_vessel)

    # Get PostgreSQL connection string from environment variable
    connection_string = os.getenv("DATABASE_URL")
    if not connection_string:
        print("Error: DATABASE_URL environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    # Load data into PostgreSQL or print SQL in dry-run mode
    load_to_postgres(flattened_data, args.table_name, connection_string, dry_run=args.dry_run)

if __name__ == "__main__":
    main()

