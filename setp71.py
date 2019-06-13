n1=input()
n=int(n1)
num=input().split()
r=0
t=0
s1=[]
for i in num:
  if r<n:
    s1.append(int(i))
    r+=1
for i in range(n-1):
  if s1[i]>s1[i+1]:
    print(s1[i],end=" ")
  else:
    print(s1[i+1],end=" ")
