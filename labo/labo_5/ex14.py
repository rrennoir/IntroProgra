import math


def distance_on_earth(coord1: tuple, coord2: tuple) -> float:

    earth_radius = 6378

    lat1_radian = math.radians(coord1[0])
    lon1_radian = math.radians(coord1[1])

    lat2_radian = math.radians(coord2[0])
    lon2_radian = math.radians(coord2[1])

    sin_part = (math.sin(lat1_radian) * math.sin(lat2_radian))
    cos_part = math.cos(lat1_radian) * math.cos(lat2_radian) * math.cos(abs(lon1_radian - lon2_radian))

    return earth_radius * math.acos(sin_part + cos_part)


print(distance_on_earth((173, 50), (-173, 150)))
