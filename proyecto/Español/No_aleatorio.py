from sys import stdin
from Utils.Find_path import animation


def no_aleatorio():
    print("Ingrese el laberinto:")
    map = []
    while True:
        col = stdin.readline().strip()
        if not col:
            break
        map.append(col)
    print("Ingrese la posicion de inicio del Pac-Man")
    print("De la forma (y ,x)")
    ini_y, ini_x = [int(c) for c in stdin.readline().strip().split()]
    try:
        if map[ini_x][ini_y] == "#":
            print("EL valor ingresado esta sobre uno de los obstaculos del laberinto")
            no_aleatorio()
    except IndexError:
        print("EL valor ingresado esta fuera del laberinto")
        no_aleatorio()
    print("Ingrese la posicion de la salida del laberinto o a donde desea llegar")
    target_y, target_x = [int(c) for c in stdin.readline().strip().split()]
    try:
        if map[target_x][target_y] == "#":
            print("EL valor ingresado esta sobre uno de los obstaculos del laberinto")
            no_aleatorio()
    except IndexError:
        print("EL valor ingresado esta fuera del laberinto")
        no_aleatorio()
    animate(map, (ini_y, ini_x), (target_y, target_x), 2)
