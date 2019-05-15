from sys import stdin


def qsort(lista):
    try:
        if not lista :
            return []
        else:
            pivote = lista[0]
            izq = qsort([x for x in lista[1:] if x < pivote])
            dech = qsort([x for x in lista[1:] if x >= pivote])
            return izq + [pivote] + dech
    except (TypeError, ValueError, IndexError):
        exit()


def elv(n, m):
    return (2**n) * m


if __name__ == '__main__':
    n = int(stdin.readline())
    color = [int(c) for c in stdin.readline().strip().split()]
    color = qsort(color)
    color.reverse()
    cont = 0
    for i in range(n):
        cont += elv(i, color[i])
    print(cont)
