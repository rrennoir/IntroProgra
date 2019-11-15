nb = int(input("Give a number: "))

i = nb
fact = 1
while i > 1:

    fact *= i
    i -= 1

print(fact)
