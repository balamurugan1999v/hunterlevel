n1=input()
n=int(n1)
num=input().split()
r=0
t=0
s1=[]
for i in num:
  if r<n:
    s1.append(int(i))
    r+=1
s1.sort()
b=len(s1)
print(s1[b-1])
