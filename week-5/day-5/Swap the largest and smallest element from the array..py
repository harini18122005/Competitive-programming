n=int(input())
arr=list(map(int,input().split()))
if len(arr)<2:
  print("")
else:
    min_index=arr.index(min(arr))
    max_index=arr.index(max(arr))
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
 
for num in arr:
  print(num,end=" ")