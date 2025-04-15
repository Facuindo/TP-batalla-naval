#tablero y esconder barcos

def tiro():

se = "s"
    while se == "s"
    tiro = input("Por favor, ingresa tu tiro")
    tiro = int(tiro)
    if tiro < 0 or tiro > 99:
        print("Numero incorrecto, proba de nuevo")
        else:
            ok ="y"
            break
        return tiro

def show_board(Barco, Erraste):
    print("    0 1 2 3 4 5 6 7 8 9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = "_ "
            if place in Erraste:
                ch = "x "
            elif place in Barco:
                ch = "o "
            row += ch
            place += 1
        print(x, " ", row)

Barco = [21]
Erraste = [20, 22, 23, 12, 13]
show_board(Barco, Erraste)