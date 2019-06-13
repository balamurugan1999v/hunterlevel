n1=input()
n=int(n1)
num=input().split()
s1=[]
s2=[]
for i in num:
  s1.append(int(i))
c=0
co=0
for i in range(n-1):
  if s1[i]>=s1[i+1]:
    if c<=co:
      c=co      
    co=0
  if s1[i]<s1[i+1]:
    co+=1
if(c<co):
  print(co+1)
else:
  print(c+1)
