#!/bin/python3

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    occr=0
    max=ar[0]
    for i in range(1,n):
        if ar[i]>max:
            max=ar[i]
    for i in range(0,n):
        if ar[i]==max:
            occr+=1
    return occr
            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()
