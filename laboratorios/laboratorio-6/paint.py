from sys import stdin

def paint(n,k):
    total = k
    mod =1000000007
    s,d = 0,k

    for i in range(2,n+1):
        s = d

        d = total*(k-1)
        d = d%mod
        total = (s+d)%mod
    return total
def main():
    n = int(stdin.readline().strip())
    k = int(stdin.readline().strip())
    print(paint(n,k))
main()
