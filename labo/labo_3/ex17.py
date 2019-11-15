def affiche_echiquier_triche():
    chess_board_size = 8
    line = 0
    while line != chess_board_size:

        if line % 2 == 0:
            print("_#_#_#_#")

        else:
            print("#_#_#_#_")

        line += 1


def affiche_echiquier():

    chess_board_size = 8
    line = 0
    chess_board = ""
    while line != chess_board_size:

        column = 0
        while column != chess_board_size:

            if line % 2 == 0:
                if column % 2 == 0:
                    chess_board += "_"
                else:
                    chess_board += "#"

            else:
                if column % 2 == 0:
                    chess_board += "#"
                else:
                    chess_board += "_"

            column += 1

        line += 1
        chess_board += '\n'

    print(chess_board)


affiche_echiquier_triche()
print("\n--------\n")
affiche_echiquier()
