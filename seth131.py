b=int(input())
a=input().split()
s1=[]
s2=[]
s3=[]
for i in a:
  if int(i)<0:
    s1.append(int(i))
  else:
    s2.append(int(i))
s1.sort()
s2.sort()
for i in s1:
  s3.append(i)
for i in s2:
  s3.append(i)
#print(s1,s2,s3)
c=b
d=0
while c>d:
  c-=1
  print(s3[c],end=" ")
  if c!=d:
    print(s3[d],end=" ")
    d=d+1
