a=input()
c=len(a)
s1=[]
for i in a:
  if i not in s1:
    s1.append(i)
for i in s1:
  print(i,end="")
