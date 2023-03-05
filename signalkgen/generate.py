#!/usr/bin/env python3
"""
gen signal k json for testing the navactor graph features
"""
import random
import math


def generate(num_boats, base_coords, nautical_miles):
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
    return signal_k_data
