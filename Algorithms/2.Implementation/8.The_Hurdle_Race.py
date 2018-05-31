#!/bin/python3

import sys

def hurdleRace(k, height):
    ans=0
    max=height[0]
    for i in range(1,len(height)):
        if height[i]>max:
            max=height[i]
    if(max>k):
        ans=max-k
    else:
        ans=0
    return ans
            
    # Complete this function

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
