n=int(input())
num=input().split()
s1=[]
s2=[]
for i in num:
  s1.append(int(i))
for i in range(n):
  c=1
  for j in range(n):
    if i!=j:
      c=s1[j]*c
  s2.append(c)
#b=len(s2)
for i in s2:
  print(i,end=" ")
