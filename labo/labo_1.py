print("Hello User !")

done = False
while not done:

    age = input("Tell me your age.\n")
    if age.isdigit():
        print("Your age in 10 years will be: {}".format((int(age) + 10)))
        done = True

    else:
        print("'{}' isn't a number, please give a number !".format(age))

print("Bye !")