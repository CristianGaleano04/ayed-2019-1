from sys import stdin


def main():
    while True:
        try:
            n = int(stdin.readline())
            k = int(stdin.readline())
            ks = k - 1
            cont = k
            for i in range(n - 1):
                cont *= ks
            print(cont)
        except ValueError:
            break


main()
