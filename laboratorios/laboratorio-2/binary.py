from sys import stdin

def bina(x,lista):
    izq = 0
    der = len(lista)-1
    if x in lista:
        while izq <= der:
            medio = (izq+der)//2
            if lista[medio]==x:
                print(medio)
                break
            elif lista[medio]>x:
                der = medio-1
            else:
                izq = medio+1
    else:
        print("-1")

    
        

def main():
    x = int(stdin.readline().strip())
    lista = list(map(int,stdin.readline().strip().split(' ')))
    bina(x,lista)
main()
