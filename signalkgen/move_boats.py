#!/usr/bin/env python3
"""
gen signal k json for testing the navactor graph features
"""
import random
import math
from datetime import datetime


def move_boats(signal_k_data):
    """
    boats should move along a vector
    """
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
    return signal_k_data
