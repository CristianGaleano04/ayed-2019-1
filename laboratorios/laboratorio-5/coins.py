from sys import stdin

def count(S, m, n): 
    
    tabla = [[0 for x in range(m)] for x in range(n+1)] 
    for i in range(m): 
        tabla[0][i] = 1
    for i in range(1, n+1): 
        for j in range(m): 
            x = tabla[i - S[j]][j] if i-S[j] >= 0 else 0
            y = tabla[i][j-1] if j >= 1 else 0
            tabla[i][j] = x + y 
  
    return tabla[n][m-1] 
  
def main():
    n = int(stdin.readline().strip())
    arr = list(map(int,stdin.readline().strip().split(',')))
    m = len(arr) 
    print(count(arr, m, n))
main()
