command = input("Give a command\n'O' to open a file\n'X' to close the program\n'F' to close the file\n'P' to print the file\nMode: ")

if command == "O":
    file_name = input("Give file name: ")
    print("Opening file '{}'".format(file_name))

elif command == "X":
    confirmation = input("Do you want the close the porgram? (o/n)")
    if confirmation == 'o':
        print("Closing the program.")

elif command == "F":
    confirmation = input("Do you want the close the file? (o/n)")
    if confirmation == 'o':
        print("Closing the file.")

elif command == "P":
    nb_print = input("How many print to make.")
    confirmation = input("Do you want to print? (o/n)")
    if confirmation == 'o':
        print("Printing file.")

else:
    print("Invalide command")