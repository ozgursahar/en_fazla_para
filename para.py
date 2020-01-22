a=100.00
z=g=c=0
for x in range(1,101):
 c=x(a/100)
 a=a-round(c,2)
 if(z>c):
  z=c
  g+=1
print(g)
