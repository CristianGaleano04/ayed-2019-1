from sys import stdin

def left(arr,d,n):
    for i in range(d):
        lr(arr,n)
def lr(arr,n):
    t = arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1] = t

def printe(arr,d):
    for i in range(d):
        print("%d"%arr[i],end=" ")

def main():
    arr = list(map(int,stdin.readline().strip().split(' ')))
    d = int(stdin.readline().strip())
    n = len(arr)
    left(arr,d,n)
    printe(arr,d)
main()        
