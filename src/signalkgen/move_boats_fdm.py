"""
gen full data model (fdm) signal k json based on input fdm and move boats
"""
import random
import math
from datetime import datetime, timedelta

def _move_boat(boat):
    """
    boat should move along a vector
    """
    interval_dur = 10
    prev_timestamp_str = boat["navigation"]["position"]["timestamp"]
    prev_timestamp = datetime.strptime(prev_timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    new_timestamp = prev_timestamp + timedelta(minutes=interval_dur)

    random_minutes = random.randint(1, interval_dur / 2)
    random_seconds = random.randint(1, 60)
    new_random_timestamp = new_timestamp + timedelta(minutes=random_minutes, seconds=random_seconds)

    new_timestamp_str = new_random_timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

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
    boat["navigation"]["position"]["timestamp"] = new_timestamp_str
    boat["navigation"]["headingMagnetic"]["timestamp"] = new_timestamp_str
    boat["navigation"]["speedOverGround"]["timestamp"] = new_timestamp_str
    boat["navigation"]["courseOverGroundTrue"]["timestamp"] = new_timestamp_str


def move_boats_fdm(signal_k_data):
    """
    boats should move along a vector
    """
    vessels = signal_k_data["vessels"]

    list(map(_move_boat, vessels.values()))

    return {"vessels": vessels}
