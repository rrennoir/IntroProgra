def tic():
    print("Tic")


def tac():
    print("Tac")


def tic_tac():
    global nb_second
    if nb_second % 2 == 0:
        tic()
    else:
        tac()

    nb_second -= 1
    if nb_second > 0:
        tic_tac()


nb_second = int(input("Give number of second: "))
tic_tac()
