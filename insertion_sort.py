# solution to https://www.hackerrank.com/challenges/insertionsort1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    deviant = arr[n-1]
    n = n - 2
    while n >= 0:
        if deviant < arr[n]:
            arr[n+1] = arr[n]
            n -= 1
        else:
            arr[n+1] = deviant
            break
        for elem in arr:
            print(elem, end=" ")
        print()
            
    if n == -1:
        arr[0] = deviant
    for elem in arr:
        print(elem, end=" ")
    print()
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
