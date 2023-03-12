"""
cat json and get csv
"""

import json
import csv
import sys

# Read the JSON data from stdin
data = json.load(sys.stdin)

# Create a CSV writer to write the output
writer = csv.writer(sys.stdout)

# Write the header row
writer.writerow(['boat', 'latitude', 'longitude'])

# Loop through each vessel object in the JSON data
for vessel in data:
    # Loop through each vessel in the vessels object
    for boat in vessel['vessels']:
        # Get the vessel's name
        name = vessel['vessels'][boat]['name']

        # Get the vessel's latitude and longitude
        position = vessel['vessels'][boat]['navigation']['position']['value']
        latitude = position['latitude']
        longitude = position['longitude']

        # Write the data to the CSV file
        writer.writerow([name, latitude, longitude])
