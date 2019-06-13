n1=input()
n=int(n1)
num=input().split()
s3=[]
for i in num:
  s3.append(int(i))
s3.sort()
b=s3[n-1]-s3[0]
print(b)
