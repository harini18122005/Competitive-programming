N = int(input())
sum_of_squares = sum(i**2 for i in range(1, N+1))
sum_squared = sum(range(1, N+1))**2
absolute_difference = abs(sum_squared - sum_of_squares)
print( absolute_difference)
