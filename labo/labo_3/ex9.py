number = float(input("Give number: "))
nb_temp = number

print("Table of {}\n---------".format(number))
while nb_temp != (number * 10):
    nb_temp += number
    print(nb_temp)
