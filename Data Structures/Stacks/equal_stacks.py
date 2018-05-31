# Enter your code here. Read input from STDIN. Print output to STDOUT
st = input()
st = list(map(int, st.split(' ')))
n1, n2, n3 = st[0], st[1], st[2]
st = input()
st1 = list(map(int, st.split(' ')))
st = input()
st2 = list(map(int, st.split(' ')))
st = input()
st3 = list(map(int, st.split(' ')))
h1, h2, h3 = sum(st1), sum(st2), sum(st3)
if h1 == h2 and h2 == h3:
	print(h1)
else:
	ind1 = ind2 = ind3 = 0
	res = 0
	while h1 > 0 and h2 > 0 and h3 > 0:
		if h1 == h2 and h2 == h3:
			res = h1
			break
		if h1 != min(h1, h2, h3):
			h1 -= st1[ind1]
			ind1 += 1
		if h2 != min(h1, h2, h3):
			h2 -= st2[ind2]
			ind2 += 1
		if h3 != min(h1, h2, h3):
			h3 -= st3[ind3]
			ind3 += 1
	print(res)