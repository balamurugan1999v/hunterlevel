s1=[]
s2=[]
a=int(input())
num=input().split()
r=0
for i in num:
  if r<a:
    s1.append(int(i))
    s2.append(int(i))
    r+=1
s2.sort()
b=0
for i in range(0,a,1):
  if s1[i]==s2[i]:
    b=b+1
if b==a:
  print("yes")
else:
  print("no")
