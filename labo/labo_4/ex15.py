import random
import time


def joke():
    """
    Print a random joke.
    """
    joke_nb = random.randint(1, 5)

    if joke_nb == 1:
        print("Insert joke n°1 here.")

    elif joke_nb == 2:
        print("Insert joke n°2 here.")

    elif joke_nb == 3:
        print("Insert joke n°3 here.")

    elif joke_nb == 4:
        print("Insert joke n°4 here.")

    elif joke_nb == 5:
        print("Insert joke n°5 here.")

    else:
        print("Insert joke n°6 here.")


def riddle():
    """
    Make a riddle for the user to guess a number between 1 and 100.
    """
    mystery_nb = random.randint(1, 100)
    print("Find the number between 1 and 100.")

    nb = int(input("Give a number: "))
    while nb != mystery_nb:

        if nb > mystery_nb:
            print("Trop grand")

        else:
            print("trop petit")

        nb = int(input("Give a number: "))

    print("Gagné")


def count():
    """
    Count down the number of second given by the user.
    """

    time_counter = int(input("How much time to count: "))
    while time_counter > 0:

        print(time_counter)
        time_counter -= 1
        time.sleep(1)

    print("The 10 second are over.")


print("I'm Bot!")
print("Action:\n1) joke\n2) riddle\n3) count\n4) quit")
message = input("Action: ")
while message != "quit":

    if message == "joke":
        joke()

    elif message == "riddle":
        riddle()

    elif message == "count":
        count()

    message = input("Action: ")

print("Bye !")
