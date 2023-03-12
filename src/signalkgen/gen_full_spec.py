#!/usr/bin/env python3
"""
gen signal k json for testing the navactor graph features
"""
import copy
import random
import json
from signalkgen.move_boats import move_boats
from signalkgen.generate import generate

def gen_full_spec(args):
    """
    gen json for full spec schema
    """
    # this is wrong - each boat in the generate dict should report just
    # the closest other boats in it's vessels stanza

    # Generate initial boat positions
    data = generate(args.num_boats, (args.latitude,
                    args.longitude), args.nautical_miles)

    reporting_boat_uuid = random.choice(list(data.keys()))

    signal_k_data = {
        "version": "1.0.0",
        "self": f"{reporting_boat_uuid}",
        "vessels": data["vessels"],
        "sources": {
            "self": {
                "type": "internal",
                "src": "signalkgen"
            }
        }
    }
    boat_data = [signal_k_data]

    # Move boats and print new positions
    for _ in range(args.iterations):
        data = copy.deepcopy(move_boats(data))
        signal_k_data = {
            "version": "1.0.0",
            "self": f"{reporting_boat_uuid}",
            "vessels": data["vessels"],
            "sources": {
                "self": {
                    "type": "internal",
                    "src": "signalkgen"
                }
            }
        }
        boat_data.append(signal_k_data)

    # Convert list of dictionaries to JSON string
    print(json.dumps(boat_data, indent=2))
