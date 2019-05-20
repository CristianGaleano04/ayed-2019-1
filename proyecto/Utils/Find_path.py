from tkinter import *
from tkinter import messagebox
from Utils.Graph import Graph
from time import sleep
from collections import deque


def draw_gp(graph, canvas, start, goal):
    x1, y1 = 0, 0
    x2, y2 = 20, 20
    cont = 0
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if (col, row) == start:
                color = "#EDF50E"
            elif (col, row) == goal:
                color = "#9F0808"
            elif graph[row][col] == "#":
                color = "#3610CD"
            else:
                if graph[row][col] == "G":
                    if cont == 0:
                        color = "#ff6600"
                        cont += 1
                    elif cont == 1:
                        color = "#ff4000"
                        cont += 1
                    elif cont == 2:
                        color = "#ff6666"
                        cont += 1
                    else:
                        color = "#ff33cc"
                else:
                    color = "#0C0D00"
            line = None if graph[row][col] == "#" else "white"
            line2 = None if graph[row][col] != "#" else "white"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=line, width=1)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=line2, width=1)
            x1 += 20
            x2 += 20
        x1 = 0
        x2 = 20
        y1 += 20
        y2 += 20


def animation(map, start, goal, id):
    global sts
    tk = Tk()
    w = len(map[0]) * 25
    h = len(map) * 25
    if w > 1366:
        w = 1366
    if h > 768:
        h = 768
    canvas = Canvas(tk, bg="#B0A1EC", width=w, height=h)
    tk.title("PAC-MAN")
    canvas.pack()
    gp = Graph(map)
    draw_gp(gp.graph, canvas, start, goal)
    sts = False

    def bfs():
        global sts
        btn.config(state=DISABLED)
        queue = deque([start])
        came_from = dict(start=None)
        while queue:
            current = queue.popleft()
            if current == goal:
                sts = True
                color = "#9F0808"
                canvas.create_rectangle(current[0] * 20, current[1] * 20, current[0] *
                                        20 + 20, current[1] * 20 + 20, fill=color, outline="white")
                break
            else:
                if current == start and current != goal:
                    color = "#EDF50E"
                    canvas.create_rectangle(current[0] * 20, current[1] * 20, current[0] * 20 + 20, current[1]
                                            * 20 + 20, fill=color, outline="white")
                elif current != goal and current != "G":
                    color = "#99ffff"
                    canvas.create_rectangle(current[0] * 20, current[1] * 20, current[0] * 20 + 20, current[1]
                                            * 20 + 20, fill=color, outline="white")
            tk.update()
            sleep(0.009)
            for next in gp.edges[current]:
                if next not in came_from:
                    queue.append(next)
                    came_from[next] = current
        current = goal
        path = []
        while current != start:
            try:
                path.append(current)
                current = came_from[current]
            except KeyError:
                break
        path.append(start)
        path.reverse()
        if not sts:
            if id == 1:
                messagebox.showinfo("End", "Is not posibble not reach the target")
            else:
                messagebox.showinfo("Fin", "No es posible llegar al objetivo")
        else:
            for step in path:
                if step == goal:
                    continue
                if step == start:
                    continue
                else:
                    canvas.create_oval(step[0] * 20, step[1] * 20, step[0] * 20 + 20, step[1]
                                            * 20 + 20, fill="#f4f442", outline="white")
                tk.update()
                sleep(0.009)

            def result():
                window = Tk()
                window.title("PAC-MAN RESULTS")
                window.configure(background="#0059b3")
                canvas_2 = Canvas(window,bg="#0059b3", width=w, height=h)
                btn_ext_2 = Button(window, text=" Exit  ", command=window.destroy)
                btn_ext_2.place(x=(w - 40), y=52)
                Label(window, text="RESULTS", font="Times 30 bold underline").pack()
                Label(window, text="Movements:", font="Times 20 bold").pack()
                for i in range(len(path[1:])):
                    try:
                        Label(window, text=str(path[i]) + "  " + "->" + "  " + str(path[i+1]),
                              font="Helvetica 10 italic").pack()
                    except IndexError:
                        Label(window, text=str(path[i]), font="Helvetica 10 italic").pack()
                        break
                canvas_2.pack()
                window.mainloop()

            if id == 1:
                messagebox.showinfo("FINISH", "Target reached")
                btn_result = Button(canvas, text="Results",command=result)
                if w < 1000 and h < 600:
                    btn_result.place(x=(w - 40), y=52)
                else:
                    btn_result.place(x=(w - 40), y=52)
            else:
                messagebox.showinfo("Terminado", "Objetivo alcanzado")
    if id == 1:
        btn = Button(text="Start ", command=bfs)
        btn_ext = Button(canvas, text=" Exit  ", command=tk.destroy)
        if w < 1000 and h < 600:
            btn.place(x=(w - 40), y=1)
            btn_ext.place(x=(w - 40), y=26)
        else:
            btn.place(x=w-40, y=1)
            btn_ext.place(x=w-40, y=26)
        tk.mainloop()
    else:
        btn = Button(text="Inicio ", command=bfs)
        btn_ext = Button(canvas, text=" Salir  ", command=tk.destroy)
        if w < 1000 and h < 600:
            btn.place(x=(w - 40), y=1)
            btn_ext.place(x=(w - 40), y=26)
        else:
            btn.place(x=w - 40, y=1)
            btn_ext.place(x=w - 40, y=26)
        tk.mainloop()
