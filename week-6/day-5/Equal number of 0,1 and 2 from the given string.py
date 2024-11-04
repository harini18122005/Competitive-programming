s = input()
count0 = 0
count1 = 0
count2 = 0

for ch in s:
    if ch == '0':
        count0 += 1
    elif ch == '1':
        count1 += 1
    elif ch == '2':
        count2 += 1

if count0 == count1 == count2:
    print("Yes")
else:
    print("No")
