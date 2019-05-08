from Others.Heaps import MinHeap
from sys import stdin

if __name__ == '__main__':
    while True:
        a = [int(c) for c in stdin.readline().strip().split()]
        if not a:
            break
        n = MinHeap()
        for i in range(len(a)):
            n.insert_key(a[i] * -1)
        for j in range(len(n.A)):
            n.A[j] *= -1
        print(*n.A)
