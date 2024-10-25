n1,n2=map(int,input().split())
x=max(n1,n2)
gcd=1
for i in range(1,x+1):
  if n1%i==0 and n2%i==0:
    gcd=i
print(gcd,end=" ") 
   