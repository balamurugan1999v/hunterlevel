n1=input()
n=int(n1)
num=input().split()
s3=[]
s1=[]
for i in num:
  s1.append(int(i))
c=0
c1=0
for i in range(0,n-1):
  c=0
  co=i+1
  for j in range(i+1,n):
    if s1[i]>s1[j]:
      c+=1
  if c==(n-co):
    s3.append(s1[i])
    c1+=1
for i in range(c1):
  print(s3[i],end=" ")
print(s1[n-1],end="")
s3.append(s1[n-1])
s3.sort()
print('\n',end="")
print(s3[c1])

