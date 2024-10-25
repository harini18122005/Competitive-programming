num = int(input())
smallest = num
largest = num

while num != 1:
    num=int(input())
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(largest, end=" ")
print(smallest, end=" ")
 