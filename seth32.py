n=int(input())
a=input().split()
s1=[]
s2=[]
s3=[]
y=0
for i in a:
  s1.append(int(i))
s2=s1
while(1):
  s3=s2[1::2]
  del s2
  s2=s3
  y=len(s3)
  if y==1:
    j=s3[0]
    break
for i in range(n):
  if s1[i]==j:
    print(i)
    break
