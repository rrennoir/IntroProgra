mystery_nb = 42
found = False
nb_of_try = 0

print("5 try maximum.")
while not found and nb_of_try < 5:
    nb = float(input("Give a number: "))

    if nb > mystery_nb:
        print("Trop grand")

    elif nb < mystery_nb:
        print("trop petit")

    else:
        print("Gagné")
        found = True

    nb_of_try += 1
