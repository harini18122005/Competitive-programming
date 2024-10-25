
n=int(input())
vec = []
for i in range(1, n+1):
    vec.append(int(input()))
print("largest=",end="")
print(max(vec))
print("smallest=",end="")
print(min(vec))