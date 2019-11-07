nb = float(input("Give a number: "))
nb_temp = nb-1

while nb_temp > 0:
    nb *= nb_temp
    nb_temp -= 1

print(nb)
