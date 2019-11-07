mystery_nb = 42
found = False

while not found:
    nb = float(input("Give a number: "))

    if nb > mystery_nb:
        print("Trop grand")

    elif nb < mystery_nb:
        print("trop petit")

    else:
        print("Gégné")
        found = True
