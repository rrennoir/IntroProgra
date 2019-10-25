# Exercice 11

number = int(input("Give a integer between 0 and 15: "))
if number <= 15 and number >= 0:
    number_tmp = number
    bit_number = ""

    if number_tmp // 8 == 1:
         bit_number += "1"
         number_tmp -= 8
    else:
        bit_number += "0"

    if number_tmp // 4 == 1:
         bit_number += "1"
         number_tmp -= 4
    else:
        bit_number += "0"

    if number_tmp // 2 == 1:
        bit_number += "1"
        number_tmp -= 2
    else:
        bit_number += "0"

    if number_tmp == 1:
        bit_number += "1"
    else:
        bit_number += "0"

    print("{} in bits is {}".format(number, bit_number))

else:
    print("This is not a number between 0 and 15")
