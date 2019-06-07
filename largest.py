s1=[]
a=int(input())
r=0
num=input().split()
for i in num:
  if r<a:
    s1.append(int(i))
    r+=1
s1.sort(reverse=True)
a1=0
for i in s1:
  a1=(a1*10)+i
print(a1)
