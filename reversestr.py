s1=[]
num=input().split()
for i in num:
  j=i[::-1]
  s1.append(j)
for i in s1:
  print(i,end=" ")
