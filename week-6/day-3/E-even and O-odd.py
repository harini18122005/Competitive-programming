n=int(input())
array=map(int,input().split())
flag=1
for i in array:
  if i%2==0:
    print("E")
    flag=0
    break
if flag==1:
  print("O")    

