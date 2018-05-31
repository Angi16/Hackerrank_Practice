#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    
    sum=0
    n=len(arr)
    for i in range(n):
        sum+=arr[i]
    minsum=sum
    maxsum=0
    for i in range(n):
        if(sum-arr[i]>maxsum):
            maxsum=sum-arr[i]
        if(sum-arr[i]<minsum):
            minsum=sum-arr[i]
    print(minsum,maxsum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)