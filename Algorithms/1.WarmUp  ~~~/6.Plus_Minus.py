#!/bin/python3

import os
import sys
from decimal import *
getcontext().prec = 6
def plusMinus(arr):
    n=len(arr)
    ctz=0
    ctp=0
    ctn=0
    for i in range(n):
        if (arr[i]<0):
            ctn+=1
        elif (arr[i]>0):
            ctp+=1
        elif (arr[i]==0):
            ctz+=1
    zf=ctz/n
    pf=ctp/n
    nf=ctn/n
    print('%.6f'%pf)
    print('%.6f'%nf)
    print('%.6f'%zf)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
