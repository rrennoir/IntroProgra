
valide_input = False
while not valide_input:
    euro_value = input("Montant en Euro: ")
    change_rate = input("Montant de change: ")

    if euro_value.isdigit() and change_rate.isdecimal():
        valide_input = True
        euro_value = float(euro_value)
        change_rate = float(change_rate)

    else:
        print("Entrée(s) invalide !\n{} ou {} n'est pas un chiffre".format(euro_value, change_rate))

dollars_value = euro_value * change_rate
print("{:.2f} Euros vaut {:.2f} Dollars".format(euro_value, dollars_value))