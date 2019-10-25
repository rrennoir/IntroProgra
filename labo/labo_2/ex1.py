exchange_rate = 1.09
euro_value = float(input("Montant en Euros: "))

dollars_value = euro_value * exchange_rate

print("Euros ", euro_value, "vaut", dollars_value, "Dollars")
## print("%.2f Euros vaut %.2f Dollars" % (euro_value, dollars_value))
## print("{:.2f} Euros vaut {:.2f} Dollars".format(euro_value, dollars_value))