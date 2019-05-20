from sys import stdin
from Utils.Find_path import animate
import random


def aleatorio():
    print("Escoga entre las siguientes opciones:")
    print("1. Laberinto Pequeño  (Min:5x5 - Max:10x10)")
    print("2. Laberinto Mediano(Min:11x11 - Max:30x30)")
    print("3. Laberinto Grande (Min:31x31 - Max:60x60)")
    print("La opcion con los fantasmas solo esta disponible en la verison del laberinto mediano y grande")
    op = str(stdin.readline().strip())
    print("---------------------------------------------------------------------")
    if op == "1":
        opciones = ["#", " ", " "]
        x = random.randrange(5, 10)
        y = random.randrange(5, 10)
        map = []
        for i in range(x):
            fil = ""
            for j in range(y):
                fil += random.choice(opciones)
            map.append(fil)
        inicial = [-1, -1]
        while True:
            ini_x = random.randrange(0, len(map))
            ini_y = random.randrange(0, len(map[0]))
            if map[ini_x][ini_y] != "#":
                inicial[0] = ini_y
                inicial[1] = ini_x
                break
        final = [-1, -1]
        while True:
            fin_x = random.randrange(0, len(map))
            fin_y = random.randrange(0, len(map[0]))
            if map[fin_x][fin_y] != "#":
                final[0] = fin_y
                final[1] = fin_x
                break
        animate(map, (inicial[0], inicial[1]), (final[0], final[1]), 2)
    elif op == "2":
        opciones = ["#", " ", " ", "G", "G", "G", "G"]
        opciones_sg = ["#", " ", " "]
        x = random.randrange(11, 20)
        y = 31
        map = []
        for i in range(x):
            fil = ""
            for j in range(y):
                if i > 4:
                    opt = random.choice(opciones)
                    fil += opt
                    if opt == "G":
                        opciones.pop()
                else:
                    opt = random.choice(opciones_sg)
                    fil += opt
            map.append(fil)
        inicial = [-1, -1]
        while True:
            ini_x = random.randrange(0, len(map))
            ini_y = random.randrange(0, len(map[0]))
            if map[ini_x][ini_y] != "#":
                inicial[0] = ini_y
                inicial[1] = ini_x
                break
        final = [-1, -1]
        while True:
            fin_x = random.randrange(0, len(map))
            fin_y = random.randrange(0, len(map[0]))
            if map[fin_x][fin_y] != "#":
                final[0] = fin_y
                final[1] = fin_x
                break
        animate(map, (inicial[0], inicial[1]), (final[0], final[1]), 2)
    elif op == "3":
        opciones = ["#", " ", " ", " ", "G", "G", "G", "G"]
        opciones_sg = ["#", " ", " ", " "]
        x = random.randrange(21, 31)
        y = 31
        map = []
        for i in range(x):
            fil = ""
            for j in range(y):
                if i > 4:
                    opt = random.choice(opciones)
                    fil += opt
                    if opt == "G":
                        opciones.pop()
                else:
                    opt = random.choice(opciones_sg)
                    fil += opt
            map.append(fil)
        inicial = [-1, -1]
        while True:
            ini_x = random.randrange(0, len(map))
            ini_y = random.randrange(0, len(map[0]))
            if map[ini_x][ini_y] != "#":
                inicial[0] = ini_y
                inicial[1] = ini_x
                break
        final = [-1, -1]
        while True:
            fin_x = random.randrange(0, len(map))
            fin_y = random.randrange(0, len(map[0]))
            if map[fin_x][fin_y] != "#":
                final[0] = fin_y
                final[1] = fin_x
                break
        animate(map, (inicial[0], inicial[1]), (final[0], final[1]), 2)
    else:
        print("Valor ingresado incorrecto")
        aleatorio()




indow = Tk()
                window.title("PAC-MAN RESULTS")
                window.configure(background="#0059b3")
                canvas_2 = Canvas(window,bg="#0059b3", width=w, height=h)
                btn_ext_2 = Button(window, text=" Exit  ", command=window.destroy)
                btn_ext_2.place(x=(w - 40), y=52)
                Label(window, text="RESULTS", font="Times 30 bold underline").pack()
                Label(window, text="Movements:", font="Times 20 bold").pack()
                for i in range(len(path[1:])):
                    try:
                        Label(window, text=str(path[i]) + "  " + "--->" + "  " + str(path[i+1]),
                              font="Helvetica 10 italic").pack()
                    except IndexError:
                        Label(window, text=str(path[i]), font="Helvetica 10 italic").pack()
                        break
                canvas_2.pack()
                window.mainloop()
