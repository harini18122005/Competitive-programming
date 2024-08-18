class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Step 1: Sort the array
        result = []
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate for the first element
                continue
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate for the second element
                    continue
                
                left, right = j + 1, len(nums) - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third and fourth elements
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

