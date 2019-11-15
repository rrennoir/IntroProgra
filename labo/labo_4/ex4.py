def print_ip(nb1, nb2, nb3, nb4):

    if ((0 <= nb1 <= 255) and (0 <= nb2 <= 255) and
            (0 <= nb3 <= 255) and (0 <= nb4 <= 255)):
        print(nb1, nb2, nb3, nb4, sep=".")

    else:
        print("Invalide adresse.")


print_ip(192, 168, 1, 1)
print_ip(192, 168, -1, 1)
print_ip(163, 1, 222, 256)
