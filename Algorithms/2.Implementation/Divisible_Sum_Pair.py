import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int,input().strip().split(' ')))
res = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if (a[i] + a[j]) % k == 0:
            res += 1
print (res)