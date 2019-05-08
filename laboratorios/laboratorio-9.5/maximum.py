from queue import PriorityQueue
from Others.Heaps import MinHeap
from sys import stdin


def sum_combination(a_1, b_1, k):
    x = MinHeap(a_1)
    y = MinHeap(b_1)
    m = x.heap_sort()
    n = y.heap_sort()
    a = m[::-1]
    b = n[::-1]
    queue = PriorityQueue()
    for i in range(k):
        for j in range(k):
            aux = a[i] + b[j]
            queue.put(-aux)
    cont = 0
    while cont < k:
        print(queue.get() * -1)
        cont += 1


if __name__ == '__main__':
    while True:
        a = [int(c) for c in stdin.readline().strip().split()]
        if not a:
            break
        b = [int(c) for c in stdin.readline().strip().split()]
        k = int(stdin.readline())
        sum_combination(a, b, k)
