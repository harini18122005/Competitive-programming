num_elements = int(input(" "))
array = list(map(int, input(" ").split()))
n = int(input(" "))
result = []
for i in range(n):
    result.append(array[i])
    result.append(array[n + i])
print(result)
