s1=[]
s2=[]
a=int(input())
num=input().split()
r=0
for i in num:
  if r<a:
    s1.append(int(i))
    r+=1
b=a
n=0
tt=0
for i in range(0,a,1):
  for j in range(i,a):
    if j!=i:
      if s1[i]==s1[j]:
        tt=1
        while (i>=n and j<b):
          n=i
          b=j
          c=s1[i]
if tt==1:
  print(c)
else:
  print("unique")
