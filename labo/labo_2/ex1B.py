change_rate = 1.09

valide_input = False
while not valide_input:
    euro_value = input("Montant en Euro: ")
    if euro_value.isdigit():
        valide_input = True
        euro_value = int(euro_value)
    else:
        print("Entrée invalide!\n{} n'est pas un chiffre".format(euro_value))

dollars_value = euro_value * change_rate
print("{:.2f} Euros vaut {:.2f} Dollars".format(euro_value, dollars_value))