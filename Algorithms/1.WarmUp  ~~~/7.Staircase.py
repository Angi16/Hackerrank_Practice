#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    for i in range(n):
	    print(' '*(n-1-i)+'#'*(n-(n-i-1)))

if __name__ == '__main__':
    n = int(input())

    staircase(n)