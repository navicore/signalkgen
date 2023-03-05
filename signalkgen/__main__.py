#!/usr/bin/env python3
"""
gen signal k json for testing the navactor graph features
"""
import argparse
from signalkgen.move_boats import move_boats
from signalkgen.generate import generate

def main():
    """
    entry point
    """
    parser = argparse.ArgumentParser(description='Generate and move boats in Signal K format')
    parser.add_argument('--num-boats', type=int, default=5, help='Number of boats to generate')
    parser.add_argument('--latitude', type=float, default=37.7749,
                        help='Base latitude for generating boats')
    parser.add_argument('--longitude', type=float, default=-122.4194,
                        help='Base longitude for generating boats')
    parser.add_argument('--nautical-miles', type=float, default=10,
                        help='Range in nautical miles for generating boats')
    parser.add_argument('--iterations', type=int, default=3,
                        help='Number of iterations to move boats')
    args = parser.parse_args()

    # Generate initial boat positions
    data = generate(args.num_boats, (args.latitude,
                                                   args.longitude), args.nautical_miles)
    print("Initial boat positions:")
    print(data)

    # Move boats and print new positions
    for i in range(args.iterations):
        data = move_boats(data)
        print(f"Boat positions after iteration {i + 1}:")
        print(data)


if __name__ == "__main__":
    main()
