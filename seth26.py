n1=input()
n=int(n1)
num=input().split()
r=0
t=0
s1=[]
s2=[]
for i in num:
  if r<n:
    s1.append(int(i))
    r+=1
s2=s1[::-1]
b=len(s2)
for i in s2:
  if t<b-1:
    print(i,end="->")
    t+=1
print(s2[b-1],end="")
