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
    num = arr[n - 1]
    for i in range(n - 1):
        if arr[n - i - 2] > num:
            arr[n - i - 1] = arr[n - i - 2]
            print(" ".join(map(str, arr)))
        else:
            arr[n - i - 1] = num
            print(" ".join(map(str, arr)))
            break
    if num < arr[0]:
        arr[0] = num
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
