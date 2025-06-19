def crear_tablero():
    import random
    tablero = [[0 for rf in range(5)] for rc in range(5)]
    luces = random.randint(5, 15)
    cont = 0
    
    while cont<luces:
        fila = random.randint(0, 4)
        col = random.randint(0, 4)
        if tablero[fila][col]==0:
            tablero[fila][col]=1
            cont = cont+1
    return tablero

def mostrar_tablero(tablero):
    print("\n  1 2 3 4 5")
    for fila_num in range(5):
        print(fila_num + 1, end=" ")
        for col_num in range(5):
            print(tablero[fila_num][col_num], end=" ")
        print()

def cambiar_luz(tablero, fila, col):
    tablero[fila][col] = 1 - tablero[fila][col]
    if fila > 0:
        tablero[fila-1][col] = 1 - tablero[fila-1][col]
    if fila < 4:
        tablero[fila+1][col] = 1 - tablero[fila+1][col]
    if col > 0:
        tablero[fila][col-1] = 1 - tablero[fila][col-1]
    if col < 4:
        tablero[fila][col+1] = 1 - tablero[fila][col+1]

def contar(tablero):
    total = 0
    for fila in range(5):
        for col in range(5):
            total = total + tablero[fila][col]
    return total

def verificar(tablero):
    for fila in range(5):
        for col in range(5):
            if tablero[fila][col] == 1:
                return 0 
    return 1 

def main():
    print("Bienvenido al juego Apaga la Luz")
    print("Ingresa coordenadas (fila y columna) entre 1 y 5")
    print("El objetivo es dejar todas las luces en 0")
    
    tablero = crear_tablero()
    jugadas = 1
    terminado = 0 
    
    while terminado == 0:
        mostrar_tablero(tablero)
        encendidas = contar(tablero)
        porcentaje = (encendidas * 100) // 25
        
        print("\nJugada:", jugadas)
        print("Luces encendidas:", porcentaje, "%")
        
        fila = int(input("Fila (1-5): "))
        col = int(input("Columna (1-5): "))
        
        if 1 <= fila <= 5 and 1 <= col <= 5:
            cambiar_luz(tablero, fila-1, col-1)
            jugadas = jugadas + 1
            terminado = verificar(tablero)
        else:
            print("Valores deben ser entre 1 y 5")
    
    mostrar_tablero(tablero)
    print("\nFelicidades! Has apagado todas las luces!")
    print("Total de jugadas:", jugadas-1)
main()