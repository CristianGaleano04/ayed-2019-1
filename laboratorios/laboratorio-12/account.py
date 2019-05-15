from sys import stdin
from collections import defaultdict


def dfs(i, emails, visited, emails_gp):
    if visited[i]:
        return
    visited[i] = True
    for j in range(1, len(accounts[i])):
        email = accounts[i][j]
        emails.add(email)
        for neighbor in emails_gp[email]:
            dfs(neighbor, emails, visited, emails_gp)


def accounts_merge(accounts):
    visited_accounts = [False] * len(accounts)
    emails_accounts_map = defaultdict(list)
    res = []
    for i, account in enumerate(accounts):
        for j in range(1, len(account)):
            email = account[j]
            emails_accounts_map[email].append(i)
    for i, account in enumerate(accounts):
        if visited_accounts[i]:
            continue
        name, emails = account[0], set()
        dfs(i, emails, visited_accounts, emails_accounts_map)
        res.append([name] + sorted(emails))
    return res


if __name__ == '__main__':
    n = int(stdin.readline())
    accounts = []
    for i in range(n):
        a = stdin.readline().strip().split(",")
        accounts.append(a)
    res = accounts_merge(accounts)
    for i in res:
        print(*i)
