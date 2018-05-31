# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().split(' ')
n = int(s[0])
k = int(s[1])
c = list(map(int, input().split(' ')))
b = int(input())
ss = sum(c) - c[k]
fair = ss//2
if fair == b:
    print('Bon Appetit')
else:
    print(b - fair)