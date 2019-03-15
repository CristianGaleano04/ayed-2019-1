from sys import stdin

def contar(n):
    lista = [0 for i in range(n+1)]
    for i in range(n+1):
        if(i<=2):
            lista[i]=i
        else:
            lista[i]=lista[i-1]+(i-1)*lista[i-2]
    return lista[n]

def main():
    n = int(stdin.readline().strip())
    print(contar(n))
main()
