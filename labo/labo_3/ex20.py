def change_volume():
    global volume, change

    if change == "+":
        volume += 1

    elif change == "-":
        volume -= 1

    print("volume: ", volume)


volume = int(input("Give a volume: "))
change = input("up or down? (+ or -) ")
while change != "X":

    change_volume()
    change = input("up or down? (+ or -) ")
