def affiche_echiquier():
    chess_board_size = 8
    line = 0
    while line != chess_board_size :

        if line % 2 == 0:
            print("_#_#_#_#")

        else:
            print("#_#_#_#_")

        line += 1

affiche_echiquier()