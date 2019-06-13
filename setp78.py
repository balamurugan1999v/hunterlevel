n1,n2=input().split()
n=int(n1)
k=int(n2)
num=input().split()
arr=input().split()
s3=[]
for i in num:
  s3.append(int(i))
for i in arr:
  s3.append(int(i))
s3.sort()
for i in range(n+k):
  print(s3[i],end=" ")
