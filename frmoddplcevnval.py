a=int(input())
s1=[]
num=input().split()
r=0
for i in num:
  if r<a:
    s1.append(int(i))
    r+=1
for i in range(0,a):
  if i%2==0 and s1[i]%2!=0:
    print(s1[i],end=" ")
  if i%2!=0 and s1[i]%2==0:
    print(s1[i],end=" ")
