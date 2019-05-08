from Others.Heaps import MinHeap
from sys import stdin


if __name__ == '__main__':
    while True:
        a = [int(c) for c in stdin.readline().strip().split()]
        if not a:
            break
        b = [int(c) for c in stdin.readline().strip().split()]
        x = a + b
        n = MinHeap()
        for i in range(len(x)):
            n.insert_key(x[i] * -1)
        for j in range(len(n.A)):
            n.A[j] *= -1
        print(*n.A)
