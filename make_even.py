TEST_CASES = int(input())

def contains_even(num):
    for digit in num:
        if int(digit) % 2 == 0:
            return True
    return False

answers = [-1] * TEST_CASES
for testCase in range(TEST_CASES):
    num = input()
    if int(num[-1]) % 2 == 0:
        answers[testCase] = 0
    elif int(num[0]) % 2 == 0:
        answers[testCase] = 1
    elif contains_even(num):
        answers[testCase] = 2

for answer in answers:
    print(answer)
