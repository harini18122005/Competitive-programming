k = int(input())
s = input()
max_product = 0

for i in range(len(s) - k + 1):
    product = 1
    for j in range(i, i + k):
        product *= int(s[j])
    
    if product > max_product:
        max_product = product

print(max_product)
