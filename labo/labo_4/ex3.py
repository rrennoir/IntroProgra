import time


def tic_tac(second):

    while second > 0:
        if second % 2 == 0:
            print("tic")
        else:
            print("tac")

        second -= 1
        time.sleep(1)


tic_tac(4)
