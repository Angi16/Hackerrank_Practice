#!/bin/python3

import sys

def introTutorial(V, arr):
    for i in range(len(arr)):
        if arr[i]==V:
            idex=i
    return idex
    # Complete this function

if __name__ == "__main__":
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = introTutorial(V, arr)
    print(result)
