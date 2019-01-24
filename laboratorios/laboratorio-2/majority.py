from sys import stdin

def major(n,numbers):
    new = []
    for i in range(n):
        for j in range (1,n):
            if numbers[i] == numbers[j]:
                new.append(numbers[i])
    if len(new)>= n:
        return True
    else:
        return False
def main():
    n = int(stdin.readline().strip())
    numbers = list(map(int,stdin.readline().strip().split(' ')))
    print(major(n,numbers))
main()
