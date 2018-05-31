import sys
t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	mn = min(arr)
	res = sys.maxsize
	for i in range(-5, 1):
		temp = 0
		for j in range(n):
			delta = arr[j] - i - mn
			temp += delta//5 + delta%5//2 + delta%5%2
		res = min(temp, res)
	print(res)