import math

def print_circonference():
    print("Circonference: {}".format(radius * 2 * math.pi))

global radius
radius = float(input("Give me the radius of the circle: "))
print_circonference()
