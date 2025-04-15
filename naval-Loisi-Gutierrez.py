#tablero y esconder barcos

Barco = [21]
Erraste = [20, 22, 23, 12, 13]

def tiro():

    while True:
        tiro: int =  input("Por favor, ingresa tu tiro: ")
        if not tiro.isdigit() or type(int(tiro)) != int: # Si tiro no es un número
            print("Ingrese un número entero")
            continue

        tiro = int(tiro)
  
        if tiro < 0 or tiro > 99: # si tiro excede el límite
            print("Numero incorrecto, proba de nuevo")
            continue

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
    tiro()



show_board (Barco, Erraste)
