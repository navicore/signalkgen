#!/usr/bin/env python3
"""
gen signal k json for testing the navactor graph features
"""
import random
import math
import uuid
from datetime import datetime


def generate(num_boats, base_coords, nautical_miles):
    """
    gen signal k json
    """
    vessels = {}
    for i in range(1, num_boats + 1):
        boat_data = {
            "name": f"Boat {i}",
            "uuid": f"urn:mrn:signalk:uuid:{str(uuid.uuid4())}",
            "mmsi": str(123456789 + i),
            "navigation": {
                "position": {
                    "value": {
                        "latitude": base_coords[0] + (random.random() * 2 - 1) *
                        (nautical_miles / 60),
                        "longitude": base_coords[1] + (random.random() * 2 - 1) *
                        (nautical_miles / 60) / math.cos(base_coords[0] *
                                                         math.pi / 180),
                        "altitude": 0.0
                    },
                    "$source": "self",
                    "timestamp": datetime
                    .utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                }
            },
            "headingMagnetic": {
                "value": 0.0,
                "$source": "self",
                "timestamp": datetime.utcnow().strftime(
                    '%Y-%m-%dT%H:%M:%S.%fZ')
            },
            "speedOverGround": {
                "value": 0.0,
                "$source": "self",
                "timestamp": datetime.utcnow().strftime(
                    '%Y-%m-%dT%H:%M:%S.%fZ')
            },
            "courseOverGroundTrue": {
                "value": 0.0,
                "$source": "self",
                "timestamp": datetime.utcnow().strftime(
                    '%Y-%m-%dT%H:%M:%S.%fZ')
            }
        }
        vessels[f"urn:mrn:signalk:uuid:{boat_data['uuid']}"] = boat_data
    return {"vessels": vessels}
