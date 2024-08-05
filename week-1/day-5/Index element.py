
n = int(input(" "))
array = list(map(int, input(" ").split()))
x = int(input(" "))
index = -1
for i in range(n):
    if array[i] == x:
        index = i
        break
print(index)
