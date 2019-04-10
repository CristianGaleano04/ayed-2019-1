import heapq
from sys import stdin


if __name__ == '__main__':
    heap = []
    heap_aux = []
    len_p = int(stdin.readline())
    for x in range(len_p):
        a = int(stdin.readline())
        if not heap:
            heapq.heappush(heap, a)
        else:
            if len(heap) > len(heap_aux):
                if heap[0] < a:
                    b = heapq.heappushpop(heap, a)
                    heapq.heappush(heap_aux, -b)
                else:
                    heapq.heappush(heap_aux, -a)
            else:
                if -heap_aux[0] > a:
                    b = -heapq.heappushpop(heap_aux, -a)
                    heapq.heappush(heap, b)
                else:
                    heapq.heappush(heap, a)
        if len(heap) > len(heap_aux):
            print("%.1f" % heap[0])
        else:
            print("%.1f" % ((heap[0] - heap_aux[0]) / 2))
