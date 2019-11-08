def print_ip(nb1, nb2, nb3, nb4):

    if (fit_in_a_byte(nb1) and fit_in_a_byte(nb2) and
            fit_in_a_byte(nb3) and fit_in_a_byte(nb4)):
        print(nb1, nb2, nb3, nb4, sep=".")
    else:
        print("Invalide adresse.")


def fit_in_a_byte(nb):

    if nb <= 255:
        return True
    return False


print_ip(192, 168, 1, 1)
print_ip(163, 1, 222, 256)
