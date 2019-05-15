from sys import stdin
from Others.Disjoint import Disjoint
from collections import defaultdict


def accounts_merge(accounts):
    ds = Disjoint()
    mail_nm = {}
    mail_id = {}
    cont = 0
    for i in accounts:
        name = i[0]
        for j in i[1:]:
            ds.make_set(j)
            mail_nm[j] = name
            if j not in mail_id:
                mail_id[j] = i
                cont += 1
            ds.union(i[1], j)
    



if __name__ == '__main__':
    n = int(stdin.readline())
    accounts = []
    for i in range(n):
        a = stdin.readline().strip().split(",")
        accounts.append(a)
    print(accounts_merge(accounts))
