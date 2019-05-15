from sys import stdin


if __name__ == '__main__':
    [n, k], c = map(int, input().split()), list(map(int, input().split()))
    ans = 0
    last = 0
    while last < n:
        i = max([last - k] + [j for j in range(max(0, last - k + 1), min(n, last + k)) if c[j]])
        if i == last - k:
            ans = -1
            break
        ans += 1
        last = i + k
    print(ans)
