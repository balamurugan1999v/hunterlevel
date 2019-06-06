s1=[]
s2=[]
b=0
n=int(input())
item=input().split()
for i in item:
  s1.append(int(i))
for i in range(0,n-1):
  b=0
  for j in range(i+1,n):
    if s1[i]==s1[j]:
      b=b+1
      break
  if b>=1 and s1[i] not in s2:
    s2.append(s1[i])
for i in s2:
  print(i,end=" ")
