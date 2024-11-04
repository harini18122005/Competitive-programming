s, d = map(int, input().split())
if not (0 < s <= 36) or not (0 < d <= 4):
    print(-1)
else:
    digits = [0] * d
    for i in range(d):
        if s >= 9:
            digits[i] = 9
            s -= 9
        elif s > 0:
            digits[i] = s
            s = 0
        else:
            break
    if s > 0 or len(digits) < d:
        print(-1)
    else:
        result = int("".join(map(str, digits)))
        print(result)