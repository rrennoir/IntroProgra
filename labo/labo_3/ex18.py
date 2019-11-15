import math


def print_circonference():
    global radius
    print("Circonference: {}".format(radius * 2 * math.pi))


radius = float(input("Give me the radius of the circle: "))
print_circonference()
