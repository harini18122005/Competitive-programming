class Solution:
    def sumOfDivisors(self, N):
        sum_divisors = 0
        for d in range(1, N + 1):
            sum_divisors += d * (N // d)
        
        return sum_divisors