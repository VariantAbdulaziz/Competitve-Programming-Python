TEST_CASES = int(input())

def damage(stabs, k):
    ret = 0
    prevStab = stabs[0]

    for stab in stabs[1:]:
        ret += min(stab - prevStab, k)
        prevStab = stab

    return ret

def solvePoisonedDagger(stabs, h):
    l, r = 1, h
    stabs.append(stabs[-1]+h)

    while r - l > 1:
        candidate_k = (l + r)//2
        d = damage(stabs,   candidate_k)
        
        if d < h:
            l = candidate_k
        else:
            r = candidate_k

    return r if damage(stabs, l) < h else l

    

answers = [0] * TEST_CASES

for testCase in range(TEST_CASES):
    n, h = [int(order) for order in input().split()]
    stabs = [int(stab) for stab in input().split()]
    answers[testCase] = solvePoisonedDagger(stabs, h)

for answer in answers:
    print(answer)

