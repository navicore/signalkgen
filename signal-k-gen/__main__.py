#!/usr/bin/env python3
"""
gen signal k json for testing the navactor graph features
"""
import argparse
import random
import math
import json
from datetime import datetime


def generate_signal_k_data(num_boats, base_coords, nautical_miles):
    """
    gen signal k json
    """
    signal_k_data = {
        "@context": "https://signalk.org/specification/1.4.0/context.json",
        "vessels": {
            "boat-1": {
                "name": "Boat 1",
                "mmsi": "123456789",
                "navigation": {
                    "position": {
                        "latitude": base_coords[0],
                        "longitude": base_coords[1]
                    }
                },
                "heading": {
                    "trueHeading": 0.0
                },
                "speedOverGround": 0.0,
                "courseOverGroundTrue": 0.0
            }
        }
    }
    for i in range(2, num_boats + 1):
        boat_data = {
            "name": f"Boat {i}",
            "mmsi": str(123456789 + i),
            "navigation": {
                "position": {
                    "latitude": base_coords[0] + (random.random() * 2 - 1) *
                    (nautical_miles / 60),
                    "longitude": base_coords[1] + (random.random() * 2 - 1) *
                    (nautical_miles / 60) / math.cos(base_coords[0] *
                                                     math.pi / 180)
                }
            },
            "heading": {
                "trueHeading": 0.0
            },
            "speedOverGround": 0.0,
            "courseOverGroundTrue": 0.0
        }
        signal_k_data["vessels"][f"boat-{i}"] = boat_data
    return json.dumps(signal_k_data)


def move_boats(signal_k_data):
    """
    boats should move along a vector
    """
    signal_k_data = json.loads(signal_k_data)
    for boat in signal_k_data["vessels"].values():
        # calculate new position based on current position, course over ground
        # true, and speed over ground
        lat = boat["navigation"]["position"]["latitude"]
        lon = boat["navigation"]["position"]["longitude"]
        cog_true = boat["courseOverGroundTrue"]
        sog = boat["speedOverGround"]
        lat += (sog / 60) * math.cos(cog_true * math.pi / 180)
        lon += (sog / 60) * math.sin(cog_true *
                                     math.pi / 180) / math.cos(lat *
                                                               math.pi / 180)
        # update boat position, heading, and speed
        boat["navigation"]["position"]["latitude"] = lat
        boat["navigation"]["position"]["longitude"] = lon
        boat["heading"]["trueHeading"] = random.uniform(0, 360)
        boat["speedOverGround"] = random.randint(1, 15)
        boat["courseOverGroundTrue"] = boat["heading"]["trueHeading"]
    signal_k_data["@timestamp"] = datetime.utcnow().strftime(
            '%Y-%m-%dT%H:%M:%S.%fZ')
    return json.dumps(signal_k_data)


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
    data = generate_signal_k_data(args.num_boats, (args.latitude,
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
