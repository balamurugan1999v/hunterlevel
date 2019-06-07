s1=[]
a=int(input())
num=input().split()
r=0
for i in num:
  if r<a:
    s1.append(int(i))
    r+=1
o=0
t=0
for i in s1:
  if o==i:
    print(i,end=" ")
    t=1
  o=o+1
if t!=1:
  print('-1')
