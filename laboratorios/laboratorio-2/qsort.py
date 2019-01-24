from sys import stdin

def qsort(n,arr): 
    if len(arr) <= 1:
        return arr
    else:
        return qsort(n,[x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               qsort(n,[x for x in arr[1:] if x >= arr[0]])        



def main():
    n = int(stdin.readline().strip())
    arr= list(map(int,stdin.readline().strip().split(' ')))
    print(qsort(n,arr))

main()
