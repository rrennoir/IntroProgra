exchange_rate = float(input("Taux de change: "))
euro_value = float(input("Montant en Euros: "))

dollars_value = euro_value * exchange_rate

print("Euros ", euro_value, "vaut", dollars_value, "Dollars")
