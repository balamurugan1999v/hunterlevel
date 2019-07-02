a=input()
b=a[::-1]
c=len(a)
temp=0
for i in range(c):
  if a[i]!=b[i]:
    temp=1
    break
if temp==0:
  print('YES')
else:
  print('NO') 
