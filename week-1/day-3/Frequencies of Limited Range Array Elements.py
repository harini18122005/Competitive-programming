class Solution:
    def frequencyCount(self, arr, n, p):
        freq = [0] * (n + 1)
        for num in arr:
            if 1 <= num <= n:
                freq[num] += 1
        
        for i in range(n):
            arr[i] = freq[i + 1]    