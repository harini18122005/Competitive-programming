def extract_second_last_digit(number):
    if number < 10:
        return None 
    number_str = str(number)
    return int(number_str[-2])


n1 = int(input())
n2 = int(input())

second_last_digit_n1 = extract_second_last_digit(n1)
second_last_digit_n2 = extract_second_last_digit(n2)

if second_last_digit_n1 is None or second_last_digit_n2 is None:
    print("Invalid number")
else:
    
    result = second_last_digit_n1 + second_last_digit_n2
    print(result)
