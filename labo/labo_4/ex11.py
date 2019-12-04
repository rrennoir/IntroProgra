def is_prime(nb):

    i = 2
    while (i != nb) and (nb % i != 0):
        i += 1

    if nb == i:
        print(f"{nb} is prime.")

    else:
        print(f"{nb} isn't prime.")


is_prime(13)
