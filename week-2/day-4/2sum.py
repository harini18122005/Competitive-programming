class Solution:
    def twoSum(self, nums, target):
        # Initialize a hash map to store the numbers and their indices
        num_map = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement exists in the hash map
            if complement in num_map:
                # If found, return the indices of the current number and the complement
                return [num_map[complement], index]
            
            # If not found, add the current number and its index to the hash map
            num_map[num] = index