nb = 102
nb1 = 6
nb2 = 4
st = "boutun"

if type(nb) == int:
    print("nb is an int!")
else:
    print("nb isn't an int")

if len(hex(nb)) >= 4:
    print("nb is a 2 digit hex number!")
else:
    print("nb isn't a 2 digit hex number!")

if (st[0] == "b") and (st > "bouton"):
    print("st start by 'b' and is after 'bouton' in the alphabetical order")
else:
    print("st doesn't start by 'b' and isn't after 'bouton' in the alphabetical order")

if nb > 0 and ((nb % 2 == 0) ^ (nb > 100)):
    print("nb is positive and pair or otherwise strictly superior to 100")
else:
    print("nb isn't positive and pair or otherwise strictly superior to 100")

if abs(nb1 - nb2) == 1:
    print("nb1 and nb2 are consecutive")
else:
    print("nb1 and nb2 aren't consecutive")
