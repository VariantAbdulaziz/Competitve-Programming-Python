# solution to https://codeforces.com/problemset/problem/1/A

m, n, a = [int(order) for order in input().split()]

result = 0
if m % a == 0:
    if n % a == 0:
        result = m // a * n // a
    else:
        result = m // a * (n + (a - (n % a)))//a
else:
    if n % a == 0:
        result = (m + (a - (m % a)))//a * n // a
    else:
        result = (m + (a - (m % a)))//a * (n + (a - (n % a)))//a

print(result)