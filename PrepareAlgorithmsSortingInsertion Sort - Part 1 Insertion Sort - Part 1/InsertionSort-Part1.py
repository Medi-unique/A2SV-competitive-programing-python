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
    num=arr[len(arr)-1]
    for i in range(len(arr)-1):
        if arr[len(arr)-i-2]>num:
            arr[len(arr)-i-1]=arr[len(arr)-2-i]
            print(" ".join(map(str, arr)))
        else :
             arr[len(arr)-i-1]=num
             print(" ".join(map(str, arr)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
