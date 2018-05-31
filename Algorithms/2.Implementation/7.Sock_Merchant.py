import sys


n = int(input())
c = list(map(int,input().strip().split(' ')))
dic = {}
res = 0
for i in c:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1
for i in dic:
    res += dic[i]//2
print(res)