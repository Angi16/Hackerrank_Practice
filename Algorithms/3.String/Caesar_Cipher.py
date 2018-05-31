#!/bin/python

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip()) % (ord('z') - ord('a') + 1)
res = list(s)
for i, l in enumerate(res):
    if l.isalpha():
        if l.isupper():
            encode = ord(l)+k
            if encode > ord('Z'):
                encode += - ord('Z') + ord('A') - 1
            res[i] = chr(encode)
        else:
            encode = ord(l)+k
            if encode > ord('z'):
                encode += - ord('z') + ord('a') - 1
            res[i] = chr(encode)
print(''.join(res))