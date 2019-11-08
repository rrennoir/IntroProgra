def print_ip(nb1, nb2, nb3, nb4):

    if nb1 < 255 and nb2 < 255 and nb3 < 255 and nb4 < 255:
        print(nb1, nb2, nb3, nb4, sep=".")
    else:
        print("Invalide adresse.")


print_ip(192, 168, 1, 1)
print_ip(163, 1, 222, 256)
