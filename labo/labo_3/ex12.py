mystery_nb = 42

nb = int(input("Give a number: "))
while nb != mystery_nb:

    if nb > mystery_nb:
        print("Trop grand")

    else:
        print("trop petit")

    nb = int(input("Give a number: "))


print("Gagné")
