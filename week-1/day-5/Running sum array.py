n = int(input(" "))
nums = list(map(int, input(" ").split()))
running_sum = []
current_sum = 0
for num in nums:
    current_sum += num
    running_sum.append(current_sum)
print(running_sum)