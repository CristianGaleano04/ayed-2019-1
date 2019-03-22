from sys import stdin


def jolly(a,n):
    f = [False]*n

    for i in range(0,n-1):
        d = abs(a[i]-a[i+1])
        if (d==0 or d>n-1 or f[d]==True):
            return False
        f[d]=True
    return True

def main():
    a = list(map(int,stdin.readline().strip().split(' ')))
    n = len(a)
    print(jolly(a,n))
main()
