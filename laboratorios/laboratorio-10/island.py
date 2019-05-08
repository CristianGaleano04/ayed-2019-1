from sys import stdin


def island(m):
    cont = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                cont += 4
                if j > 0 and m[i][j - 1]:
                    cont -= 2
                if i > 0 and m[i - 1][j]:
                    cont -= 2
    return cont


if __name__ == '__main__':
    isl = []
    while True:
        a = [int(c) for c in stdin.readline().strip().split()]
        if not a:
            break
        isl.append(a)
    print(island(isl))
