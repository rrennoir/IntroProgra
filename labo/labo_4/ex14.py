import math


def circle_area(radius: float):
    """
    Return the area of a circle.
    Parametre:
    ----------
    Radius: Raidus of the circle. (float)
    """
    return radius ** 2 * math.pi


print(circle_area(3))
