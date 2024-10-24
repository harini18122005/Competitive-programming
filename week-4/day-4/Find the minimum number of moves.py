inp=input()
a=int(inp.split()[0])
b=int(inp.split()[1])
diff=(abs(a-b))
x=int(diff/10)
if(diff%10!=0):
    x+=1
print(x)
