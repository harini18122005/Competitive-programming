n = int(input(" "))
array = list(map(int, input(" ").split()))
element = int(input(" "))
indices = []
for i in range(n):
    if array[i] == element:
        indices.append(i)
if indices:
    print(" ".join(map(str, indices)))
else:
    print("-1")
