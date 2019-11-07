def change_volume_up():
    volume += 1
    print(volume)


def change_volume_down():
    volume -= 1
    print("volume")


global volume

volume = int(input("Give a volume."))
finish = False
while not finish:

    change = input("up or down? (+ or -) ")
    if change == "+":
        change_volume_up()

    elif change == "-":
        change_volume_down()

    elif change == "X":
        finish = True
