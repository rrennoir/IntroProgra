def change_volume():
    global volume, change

    if change == "+":
        volume += 1

    elif change == "-":
        volume -= 1

    print("volume: ", volume)


volume = int(input("Give a volume."))
finish = False
while not finish:

    change = input("up or down? (+ or -) ")
    if change == "X":
        finish = True
    else:
        change_volume()
