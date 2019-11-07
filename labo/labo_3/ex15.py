def ouvrir():
    file_name = input("Give file name: ")
    print("Opening file '{}'".format(file_name))


def fermer_prog():
    confirmation = input("Do you want the close the porgram? (o/n)")
    if confirmation == 'o':
        print("Closing the program.")


def fermer_file():
    confirmation = input("Do you want the close the file? (o/n)")
    if confirmation == 'o':
        print("Closing the file.")


def print_file():
    nb_print = input("How many print to make.")
    confirmation = input("Do you want to print? (o/n)")
    if confirmation == 'o':
        print("Printing file.")


command = input("Give a command\n'O' to open a file\n'X' to close the program"
                "\n'F' to close the file\n'P' to print the file\nMode: ")

if command == "O":
    ouvrir()

elif command == "X":
    fermer_prog()

elif command == "F":
    fermer_file()

elif command == "P":
    print_file()

else:
    print("Invalide command")
