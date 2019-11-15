mystery_nb = 42
attemps = 1

nb = int(input("Give a number: "))
while nb != mystery_nb and attemps < 5:

    if nb > mystery_nb:
        print("Trop grand")

    else:
        print("trop petit")

    attemps += 1
    nb = int(input("Give a number: "))

if mystery_nb == nb and attemps <= 5:
    print("Gagné")
else:
    print("Perdu")
