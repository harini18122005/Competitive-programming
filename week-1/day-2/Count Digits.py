class Solution:
    def evenlyDivides(self, N):
        count = 0
        original_number = N
        
        while N > 0:
            digit = N % 10
            if digit != 0 and original_number % digit == 0:
                count += 1
            N //= 10
        
        return count
