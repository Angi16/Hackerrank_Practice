#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    scr=score[0]
    maxscr=score[0]
    minscr=score[0]
    mxc=0
    mnc=0
    n=len(score)
    for i in range(1,n):
        scr=score[i]
        if(scr>maxscr):
            maxscr=scr
            mxc+=1
        if(scr<minscr):
            minscr=scr
            mnc+=1
    return(mxc,mnc)
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()