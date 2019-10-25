# A
value_1 = float(input("Valeur 1: "))
value_2 = float(input("Valeur 2: "))

print("Value 1: ", value_1, "- Value 2:", value_2)

value_temp = value_1
value_1 = value_2
value_2 = value_temp

print("Value 1:", value_1, "- Value 2:", value_2)

# B
value_1 = float(input("Valeur 1: "))
value_2 = float(input("Valeur 2: "))

print("Value 1:", value_1, "- Value 2:", value_2)

value_1, value_2 = value_2, value_1

print("Value 1:", value_1, "- Value 2:", value_2)