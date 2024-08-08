class Solution(object):
    def maxSubArray(self, nums):
        # Initialize the variables
        current_max = nums[0]
        global_max = nums[0]
        
        # Start iterating from the second element
        for num in nums[1:]:
            # Update current_max to be the maximum of adding the current number or starting new subarray
            current_max = max(num, current_max + num)
            # Update global_max if current_max is greater
            global_max = max(global_max, current_max)
        
        return global_max
