import math

def is_a_square_nb():
    if math.sqrt(nb) % 1 == 0:
        print("ok")
        
    tmp = 1
    while tmp**2 != nb:
        tmp += 1

        if nb / 2 < tmp:
            print("nop")
            return
    
    print("ok")

global nb
nb = int(input("Give a number: "))
is_a_square_nb()