import sys

A,B,C,D =input().strip().split()
A,B,C,D = sorted([int(A),int(B),int(C),int(D)])

total = [0] * (3010)
cnt = [[0 for j in range(4200)] for i in range(3010)]
for i in range(1,A+1):
    for j in range(i,B+1):
        total[j] += 1
        cnt[j][i^j] += 1
for i in range(1,3001):
    total[i] += total[i-1]
    for j in range(4101):
        cnt[i][j] += cnt[i-1][j]
res = 0
for i in range(1,C+1):
    for j in range(i,D+1):
        res += total[i] - cnt[i][i^j]
print(res)