a=input()
s1=[]
s2=[]
y=0
for i in a:
  if i not in s1:
    s1.append(i)
  else:
    s2.append(i)
b=len(s1)
c=len(s2)
d=b-c
if d==1:
  print ('yes')
else
