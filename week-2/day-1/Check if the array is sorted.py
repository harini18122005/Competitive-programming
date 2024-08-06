class Solution:
    def check(self, nums):
        # Initialize the count for the number of breaks
        break_count = 0
        n = len(nums)
        
        for i in range(n):
            # Check if the current element is less than the previous element
            if nums[i] < nums[i - 1]:
                break_count += 1
                
            # If there are more than 1 breaks, return False
            if break_count > 1:
                return False
        
        # If we have 0 or 1 breaks, the array is a rotated sorted array
        return True


