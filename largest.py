s1=[]
a=int(input())
r=0
num=input().split()
for i in num:
  if r<a:
    s1.append(i)
    r+=1
s1.sort(reverse=True)
for i in s1:
  print(i,end="")
