TEST_CASES = int(input())

def solveBinaryDeque(binaryDeque, s):
    if s > len(binaryDeque):
        return -1
    
    largestWinThatSumToS = 0
    winSum = 0

    l = r = 0
    while l < len(binaryDeque) and r < len(binaryDeque):
        if winSum <= s:
            winSum += binaryDeque[r]
            if winSum == s:
                largestWinThatSumToS = max(largestWinThatSumToS, r - l + 1)
            r += 1
        else:
            winSum -= binaryDeque[l]
            l += 1


    return n - largestWinThatSumToS if largestWinThatSumToS != 0 else -1

answers = [-1] * TEST_CASES

for testCase in range(TEST_CASES):
    n, s = [int(order) for order in input().split()]
    binaryDeque = [1 if binary == "1" else 0 for binary in input().split()]

    answers[testCase] = solveBinaryDeque(binaryDeque, s)

for answer in answers:
    print(answer)
