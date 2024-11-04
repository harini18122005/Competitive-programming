s = input()
flag = 1
for char in s:
    if char == '#':
        print("Yes")
        break
else:
    print("No")