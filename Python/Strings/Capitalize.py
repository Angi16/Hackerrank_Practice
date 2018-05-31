# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
temp=list(s)
temp[0]=temp[0].upper()
for i in range(1,len(temp)):
    if temp[i-1]==" ":
        temp[i]=temp[i].upper()
print("".join(temp))