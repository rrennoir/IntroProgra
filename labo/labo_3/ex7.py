price_no_vat = float(input("Give me the price without the VAT: "))
product_cat = input("Give me the categorie of the product (normal, important, nécessaire): ")

if product_cat == "nécéssaire":
    taxe = 0.06

elif product_cat == "important":
    taxe = 0.12

else:
    taxe = 0.21

print("The price with the WAT is: {}".format(price_no_vat * (1 + taxe)))
