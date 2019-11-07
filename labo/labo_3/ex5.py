number_1 = float(input("Give me a number: "))
number_2 = float(input("Give me anthoer number: "))
number_3 = float(input("Give me anthoer number anthoer number:"))

if number_1 in (number_2, number_3):
    print("{} has been given twice or more".format(number_1))

elif number_3 in (number_1, number_2):
    print("{} has been given twice or more".format(number_3))
