from sys import stdin
from collections import deque


def jesse_cookies(n, k, queue, list_2=[]):
    max_comb = 0
    queue_aux = deque()
    while queue:
        if queue and queue_aux and (len(queue) == 1):
            while queue_aux:
                queue.append(queue_aux.popleft())
        if queue and queue_aux and (queue_aux[0] <= queue[0]):
            queue.appendleft(queue_aux.popleft())
        if queue and (len(list_2) == 0) and (k <= queue[0]):
            break
        c_k = queue.popleft()
        list_2.append(c_k)
        if len(list_2) == 2:
            new_c_k = list_2[0] + (list_2[1] * 2)
            list_2 = []
            queue_aux.append(new_c_k)
            max_comb += 1
    while queue_aux:
        queue.append(queue_aux.popleft())
    if any(i < k for i in queue):
        return '-1'
    else:
        return max_comb


if __name__ == '__main__':
    list_f = [int(c)for c in stdin.readline().strip().split()]
    queue = deque(sorted([int(c)for c in stdin.readline().strip().split()]))
    print(jesse_cookies(list_f[0], list_f[1], queue))
