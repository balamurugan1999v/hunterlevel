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
for i in range(n):
  if s1[i]==k:
    print(i+1)
