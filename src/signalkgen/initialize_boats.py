"""
gen signal k json for testing the navactor graph features
"""
import random
import math
import uuid
from datetime import datetime, timedelta

country_codes = {
    "200": range(0, 20),  # Test MID range for illustration purposes
    "201": range(0, 20),  # Test MID range for illustration purposes
    "202": range(0, 20),  # Test MID range for illustration purposes
    "203": range(0, 20),  # Test MID range for illustration purposes
    "204": range(0, 20),  # Test MID range for illustration purposes
    "205": range(0, 20)   # Test MID range for illustration purposes
}

def initialize_boats(args, base_coords):
    """
    gen signal k json
    """
    now = datetime.utcnow()
    init_timestamp = now - timedelta(hours=args.hours_ago)
    init_timestamp_str = init_timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    vessels = {}
    for i in range(1, args.num_boats + 1):
        # Generate MMSI based on country code, MID, and unique vessel ID
        country_code = random.choice(list(country_codes.keys()))
        mid_range = country_codes[country_code]
        mid = random.choice(mid_range)
        mid_padded = str(mid).zfill(2)
        vessel_id = random.randint(1000, 9999)
        mmsi = f"{country_code}{mid_padded}{vessel_id}"

        boat_data = {
            "name": f"Boat {i}",
            "uuid": f"urn:mrn:signalk:uuid:{str(uuid.uuid4())}",
            "mmsi": mmsi,
            "navigation": {
                "position": {
                    "value": {
                        "latitude": base_coords[0] + (random.random() * 2 - 1) *
                        (args.nautical_miles / 60),
                        "longitude": base_coords[1] + (random.random() * 2 - 1) *
                        (args.nautical_miles / 60) / math.cos(base_coords[0] *
                                                         math.pi / 180),
                        "altitude": 0.0
                    },
                    "$source": "self",
                    "timestamp": init_timestamp_str
                },
                "courseOverGroundTrue": {
                    "value": 0.0,
                    "$source": "self",
                    "timestamp": init_timestamp_str
                },
                "speedOverGround": {
                    "value": 0.0,
                    "$source": "self",
                    "timestamp": init_timestamp_str
                },
                "headingMagnetic": {
                    "value": 0.0,
                    "$source": "self",
                    "timestamp": init_timestamp_str
                }
            }
        }
        vessels[f"{boat_data['uuid']}"] = boat_data
    return {"vessels": vessels}
