from sys import stdin


def astr(n , astronauts):
    x = [len(c) for c in countries if c]

    def distance(n):
        return n * (n + 1) //2
    unpaired = sum(x == -1 for x in astronauts)
    total = distance(unpaired - 1)
    total += unpaired * sum(x)
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            total += x[i] * x[j]
    return total


if __name__ == '__main__':
    num = [int(c) for c in stdin.readline().split()]
    n = num[0]
    p = num[1]
    astronauts = [-1] * n
    countries = []
    for w in range(p):
        a, b = list(map(int, stdin.readline().split()))
        if astronauts[a] > -1 and astronauts[b] > -1:
            if astronauts[a] != astronauts[b]:
                k = astronauts[b]
                countries[astronauts[a]].extend(countries[k])
                for i in countries[k]:
                    astronauts[i] = astronauts[a]
                countries[k] = []
        elif astronauts[a] > -1 and astronauts[b] == -1:
            astronauts[b] = astronauts[a]
            countries[astronauts[a]].append(b)
        elif astronauts[a] == -1 and astronauts[b] > -1:
            astronauts[a] = astronauts[b]
            countries[astronauts[b]].append(a)
        else:
            astronauts[b] = astronauts[a] = len(countries)
            countries.append([a, b])
    res = astr(n, astronauts)
    print(res)
