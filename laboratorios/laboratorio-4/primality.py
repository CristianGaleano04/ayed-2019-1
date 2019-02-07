from sys import stdin

def primos(p,q):
    for i in range(p):
        for j in range(2,q[i]):
            if q[i]%j==0:
                print ("No" )
                break
            else:
                print("Si /n")
                break
            

def main():
    p = int(stdin.readline().strip())
    q = list(map(int,stdin.readline().strip().split(' ')))
    primos(p,q) 
main()
