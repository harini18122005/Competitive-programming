string=input()
strt,length=map(int,input().split())
x=""
for i in range(strt,len(string)):
    x+=string[i]
    if(len(x)==length):
      break
print(x)

