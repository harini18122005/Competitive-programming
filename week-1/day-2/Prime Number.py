import math

class Solution:
    def isPrime(self, N):
        if N <= 1:
            return 0
        if N <= 3:
            return 1 
        if N % 2 == 0 or N % 3 == 0:
            return 0
        for i in range(5, int(math.sqrt(N)) + 1, 6):
            if N % i == 0 or N % (i + 2) == 0:
                return 0
        
        return 1
