class Solution:
    def maxProduct(self, nums):
        # Initialize variables
        max_prod = min_prod = result = nums[0]
        
        # Traverse the array
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            
            # Update max_prod and min_prod
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])
            
            # Update the result
            result = max(result, max_prod)
        
        return result
