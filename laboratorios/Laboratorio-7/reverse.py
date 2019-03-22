from sys import stdin

def reverse(a):
    str = ""
    for i in a:
        str = i + str
    return str
def main():
    a = stdin.readline().strip()
    print(reverse(a))
main()
