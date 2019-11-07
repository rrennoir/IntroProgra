def tic():
    print("Tic")

def tac():
    print("Tac")


nb_second = int(input("Give number of second: "))

while nb_second > 0:

    if nb_second % 2 == 0:
        tic()
    else:
        tac()
    nb_second -= 1