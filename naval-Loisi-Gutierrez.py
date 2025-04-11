#tablero y esconder barcos

def show_board(Barco, Nobarco, completo):
    print("  0 1 2 3 4 5 6 7 8 9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = "  "
            if place in Nobarco:
                ch = " x"
            elif place in Barco:
                ch = " o"
            elif place in completo:
                ch = " 0"
            row += ch
            place += 1
        print(x, " ", row)


Barco = [21, 22]
Nobarco = [20, 24, 12, 13]
completo = [23]

show_board(Barco, Nobarco, completo)