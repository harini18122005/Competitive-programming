class Solution(object):
    def nextPermutation(self, nums):
        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If such an element is found, find the element to swap with
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap the elements
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the sequence to the right of the swapped element
        self.reverse(nums, i + 1, len(nums) - 1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

