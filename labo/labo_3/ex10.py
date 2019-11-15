nb = int(input("Give a number: "))
somme = 0
while nb >= 0:

    somme += nb
    nb = int(input("Give a number: "))

print("Somme: {}".format(somme))
