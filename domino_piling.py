# solution to https://codeforces.com/problemset/problem/50/A

m, n = [int(order) for order in input().split()]

dominoNo = (n * (m // 2)) + ((m % 2) * (n // 2))

print(dominoNo)