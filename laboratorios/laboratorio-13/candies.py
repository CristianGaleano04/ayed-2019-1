from sys import stdin


def candies(n, kids):
    m = 0
    while n != 0:
        kids.append(int(input()))
        n -= 1
        m += 1
    candies_pos= [[0 for i in range(m)] for j in range(3)]
    left = candies_pos[0]
    right = candies_pos[1]
    num = candies_pos[2]
    p = 1
    while p < m:
        if kids[p] > kids[p - 1]:
            left[p] = left[p - 1] + 1
        p += 1
    p = m - 2
    while p >= 0:
        if kids[p] > kids[p + 1]:
            right[p] = right[p + 1] + 1
        p -= 1
    p = 0
    while p < m:
        num[p] = 1 + max(left[p], right[p])
        p += 1
    print(sum(num))


if __name__ == '__main__':
    n = int(stdin.readline())
    kids = []
    candies(n, kids)
