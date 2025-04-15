#tablero y esconder barcos

def show_board(Barco, Nobarco):
    print("    0 1 2 3 4 5 6 7 8 9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = "_ "
            if place in Nobarco:
                ch = "x "
            elif place in Barco:
                ch = "o "
            row += ch
            place += 1
        print(x, " ", row)

Barco = [21]
Nobarco = [20, 22, 23, 12, 13]
show_board(Barco, Nobarco)