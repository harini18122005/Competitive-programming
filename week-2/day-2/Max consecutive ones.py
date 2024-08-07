class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                if current_count > max_count:
                    max_count = current_count
                current_count = 0
                return max(max_count, current_count)
