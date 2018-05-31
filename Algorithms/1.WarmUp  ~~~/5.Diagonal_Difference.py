#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    i=0
    n=len(a)
    d1,d2=0,0
    diff=0
    for j in range(n):
        d1+=a[j][j]
        d2+=a[i+j][n-1-j]
        diff=abs(d2-d1)
    return diff

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()