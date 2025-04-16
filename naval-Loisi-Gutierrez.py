git add naval-Loisi-Gutierrez.py

#tablero y esconder barcos

def show_board(Barco, Nobarco, completo):
    print("  0 1 2 3 4 5 6 7 8 9")
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
            ch = "  "
            if place in Nobarco:
                ch = " x"
            ch = "_ "
            if place in Erraste:
                ch = "x "
            elif place in Barco:
                ch = " o"
            elif place in completo:
                ch = " 0"
                ch = "o "
            row += ch
            place += 1
        print(x, " ", row)
    tiro()


Barco = [21, 22]
Nobarco = [20, 24, 12, 13]
completo = [23]
show_board (Barco, Erraste)


from random import randrange

N = 10  
CANTIDAD_BARCOS = 5

def crear_tablero(n):
    return [[False for _ in range(n)] for _ in range(n)]

# Colocar barcos al azar, un barco por celda
def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = randrange(len(tablero))
        col = randrange(len(tablero))
        if not tablero[fila][col]:
            tablero[fila][col] = True
            colocados += 1

# Mostrar tablero de aciertos y errores
def mostrar_tablero(tablero_disparos):
    print("Tablero de disparos:")
    print("   " + " ".join([str(i) for i in range(len(tablero_disparos))]))
    for i, fila in enumerate(tablero_disparos):
        fila_str = ["x" if c == "X" else ("o" if c else ".") for c in fila]
        print(f"{i:2} " + " ".join(fila_str))

# Ejecutar juego
barcos = crear_tablero(N)
colocar_barcos(barcos, CANTIDAD_BARCOS)
disparos = [[False for _ in range(N)] for _ in range(N)]
aciertos = 0
fallos = 0
intentos = 0

while aciertos < CANTIDAD_BARCOS:
    mostrar_tablero(disparos)
    print(f"Disparo número {intentos + 1}")
    try:
        fila = int(input("Ingresa fila (0 a N-1): "))
        col = int(input("Ingresa columna (0 a N-1): "))
        if fila < 0 or fila >= N or col < 0 or col >= N:
            print("Coordenadas fuera de rango. Intenta de nuevo.")
            continue
        if disparos[fila][col] != False:
            print("Ya disparaste allí. Intenta otra vez.")
            continue

        intentos += 1

        if barcos[fila][col]:
            print("¡Acertaste un barco!")
            disparos[fila][col] = "X"
            aciertos += 1
        else:
            print("Fallaste.")
            disparos[fila][col] = True
            fallos += 1

    except ValueError:
        print("Entrada inválida. Ingresá un número.")

mostrar_tablero(disparos)
print(f"Juego terminado en {intentos} disparos.")

 
