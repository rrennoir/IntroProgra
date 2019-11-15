print("Hello User !")

age = input("Tell me your age.\n")
while not age.isdigit():
    age = input("Tell me your age.\n")

print("Your age in 10 years will be: {}".format((int(age) + 10)))
print("Bye !")