
h = list(map(int,input().strip().split()))
word = input().strip()
height = []
for i in word:
    height += [h[ord(i) - ord('a')]]
print(len(word) * max(height))