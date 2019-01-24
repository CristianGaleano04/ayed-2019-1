from sys import stdin

def maxim(lista):
    if len(lista) > 1:
        mid = len(lista)//2
        izq = lista[:mid]
        der = lista[mid:]
        
        maxim(izq)
        maxim(der)

        i = 0
        j = 0
        k = 0
        while i<len(izq) and j<len(der):
            if izq[i] < der[j]:
                lista[k]=izq[i]
                i+=1
            else:
                lista[k] = der[j]
                j += 1
            k += 1
        while i<len(izq):
            lista[k]=izq[i]
            i+=1
            k +=1
        while j < len(der):
            lista[k]=der[j]
            j+=1
            k+=1
    
    
def main():
    lista = list(map(int,stdin.readline().strip().split(' ')))
    maxim(lista)
    print (lista[-1]*lista[-2])
main()
