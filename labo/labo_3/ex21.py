def tic():
    global nb_second
    print("Tic")
    nb_second -= 1
    if nb_second > 0:
        tac()


def tac():
    global nb_second
    print("Tac")
    nb_second -= 1
    if nb_second > 0:
        tic()


def tic_tac_triche():
    global nb_second
    if nb_second % 2 == 0:
        tic()
    else:
        tac()

    nb_second -= 1
    if nb_second > 0:
        tic_tac_triche()


nb_second = int(input("Give number of second: "))
tic()
