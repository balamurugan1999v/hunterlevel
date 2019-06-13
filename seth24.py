n1,k1=input().split()
n=int(n1)
k=int(k1)
num=input().split()
r=0
t=0
s1=[]
for i in num:
  if r<n:
    s1.append(int(i))
    r+=1
for i in range(n-1):
  for j in range(i+1,n):
    if(s1[i]+s1[j])==k:
      t=1
      break
  if t==1:
    break
if t==1:
  print("YES")
else:
  print("NO")
