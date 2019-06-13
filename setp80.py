n1=input()
n=int(n1)
num=input().split()
s3=[]
for i in num:
  s3.append(int(i))
s3.sort()
b=0
c=0
while(b==0):
  b=s3[c]-s3[0]
  c+=1
print(b)
