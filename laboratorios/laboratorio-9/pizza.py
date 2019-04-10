import heapq
from sys import stdin


def tiu_pizza(N, pizza_time):
    time_prom = 0
    min_time_now = 0
    client_w = []
    i = 0
    while i < len(pizza_time):
        if not client_w and (pizza_time[i][0] > min_time_now):
            min_time_now = pizza_time[i][0]
        while i < len(pizza_time) and pizza_time[i][0] <= min_time_now:
            heapq.heappush(client_w, tuple([pizza_time[i][1], pizza_time[i][0]]))
            i += 1
        task = heapq.heappop(client_w)
        min_time_now += task[0]
        time_prom += min_time_now - task[1]
        if i >= len(pizza_time):
            while client_w:
                task = heapq.heappop(client_w)
                min_time_now += task[0]
                time_prom += min_time_now - task[1]
    return time_prom // N


if __name__ == '__main__':
    N = int(stdin.readline())
    pizza_time = [tuple(int(v) for v in stdin.readline().split()) for v in range(N)]
    pizza_time.sort()
    print(tiu_pizza(N, pizza_time))
