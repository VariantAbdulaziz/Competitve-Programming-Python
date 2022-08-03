TEST_CASES = int(input())
def sumBinary(alist):
    res = 0
    for binary in alist:
        if binary:
            res += 1

    return res

def dfs(cache, n, s, binaryDeque, total, l, r, num):
    if total == s:
        return num
    if l > r or total < s:
        return n+1
    if (l, r) in cache:
        return cache[(l, r)]
    
    cache[(l, r)] = min(dfs(cache, n, s, binaryDeque, total-1 if binaryDeque[r] else total, l, r-1, num+1),
                        dfs(cache, n, s, binaryDeque, total-1 if binaryDeque[l] else total, l+1, r, num+1))
    
    return cache[(l, r)]

ans = []

for testCase in range(TEST_CASES):
    n, s = [int(order) for order in input().split()]
    binaryDeque = [True if binary == "1" else False for binary in input().split()]

    total = sumBinary(binaryDeque)
    cache = {}
    res = dfs(cache, n, s, binaryDeque, total, 0, n - 1, 0)
    ans.append(res if res != n+1 else -1)

for answer in ans:
    print(answer)
