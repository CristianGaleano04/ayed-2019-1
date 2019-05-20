from sys import stdin


def main_s():
    print("---------------------------------------------------------------------")
    print("Bienvenido al simulador de Pac-Man")
    print("OPCIONES:")
    print("1. Aleatorio")
    print("2. Manual")
    val = str(stdin.readline().strip())
    print("---------------------------------------------------------------------")
    if val == "2":
        from Español.No_aleatorio import no_aleatorio
        no_aleatorio()
    elif val == "1":
        from Español.aleatorio import aleatorio
        aleatorio()
main_s()
