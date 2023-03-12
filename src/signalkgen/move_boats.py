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
    vessels = signal_k_data["vessels"]
    for vessel_id in vessels:
        boat = vessels[vessel_id]
        # calculate new position based on current position, course over ground
        # true, and speed over ground
        lat = boat["navigation"]["position"]["value"]["latitude"]
        lon = boat["navigation"]["position"]["value"]["longitude"]
        cog_true = boat["navigation"]["courseOverGroundTrue"]["value"]
        sog = boat["navigation"]["speedOverGround"]["value"]
        lat += (sog / 60) * math.cos(cog_true * math.pi / 180)
        lon += (sog / 60) * math.sin(cog_true *
                                     math.pi / 180) / math.cos(lat *
                                                               math.pi / 180)
        # update boat position, heading, and speed
        boat["navigation"]["position"]["value"]["latitude"] = lat
        boat["navigation"]["position"]["value"]["longitude"] = lon
        boat["navigation"]["headingMagnetic"]["value"] = random.uniform(0, 360)
        boat["navigation"]["speedOverGround"]["value"] = random.randint(1, 15)
        boat["navigation"]["courseOverGroundTrue"]["value"] = \
            boat["navigation"]["headingMagnetic"]["value"]
        boat["navigation"]["position"]["timestamp"] = datetime.utcnow().strftime(
                    '%Y-%m-%dT%H:%M:%S.%fZ')
        boat["navigation"]["headingMagnetic"]["timestamp"] = datetime.utcnow().strftime(
                    '%Y-%m-%dT%H:%M:%S.%fZ')
        boat["navigation"]["speedOverGround"]["timestamp"] = datetime.utcnow().strftime(
                    '%Y-%m-%dT%H:%M:%S.%fZ')
        boat["navigation"]["courseOverGroundTrue"]["timestamp"] = datetime.utcnow().strftime(
                    '%Y-%m-%dT%H:%M:%S.%fZ')
    return {"vessels": vessels}
