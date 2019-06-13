n1=input()
n=int(n1)
num=input().split()
s1=[]
s2=[]
for i in num:
  if (int(i)%2)==0:
    s1.append(int(i))
  else:
    s2.append(int(i))
b=len(s1)
c=len(s2)
if(c==1):
  print(s2[0])
elif(b==1):
  print(s1[0])
