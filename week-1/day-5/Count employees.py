n = int(input(" "))
hours = list(map(int, input(" ").split()))
target = int(input(" "))
count = 0
for hour in hours:
    if hour >= target:
        count += 1
print(count)
