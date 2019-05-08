from sys import stdin


def is_max_heap(heap):
    n = len(heap)
    for i in range(int((n - 2 / 2)) + 1):
        try:
            if heap[2 * i + 1] > heap[i]:
                return False
            if 2 * i + 2 < n and heap[2 * i + 2] > heap[i]:
                return False
        except IndexError:
            pass
    return True


if __name__ == '__main__':
    while True:
        heap = [int(c) for c in stdin.readline().strip().split()]
        if not heap:
            break
        print(is_max_heap(heap))
