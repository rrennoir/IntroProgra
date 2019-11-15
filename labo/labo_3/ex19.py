def is_a_square_nb():

    global nb
    if nb ** (1/2) % 1 == 0:
        print("C'est un nombre carré.")

    else:
        print("Ce n'est pas un nombre carré.")


nb = int(input("Give a number: "))
is_a_square_nb()
