"""
gen signal k json for testing the navactor graph features
"""
import copy
import json
from signalkgen.move_boats_fdm import move_boats_fdm
from signalkgen.initialize_boats import initialize_boats

def gen_fdm(args):
    """
    gen json for full spec schema
    """
    # this is wrong - each boat in the generate dict should report just
    # the closest other boats in it's vessels stanza

    boat_data = []

    # Generate initial boat positions
    data = initialize_boats(args, (args.latitude, args.longitude))

    # for each boat, create observations from their POV
    for reporting_boat_uuid in list(data['vessels'].keys()):

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
        # set initial observation of them an all the boats they know about
        boat_data.append(signal_k_data)

        # Move boats and print new positions
        for _ in range(args.iterations):
            data = copy.deepcopy(move_boats_fdm(data))
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

    if args.compact_json:
        print(json.dumps(boat_data, separators=(',', ':')))
    else:
        print(json.dumps(boat_data, indent=2))
