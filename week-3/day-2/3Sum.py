class Solution:
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the array
        result = []
        
        for i in range(len(nums) - 2):  # Step 2: Iterate through the array
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate elements for the second pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate elements for the third pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
