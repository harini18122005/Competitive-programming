class Solution:
    def subarraySum(self, nums, k):
        prefix_sum_count = {0: 1}  # Initialize with the prefix sum 0 having one count
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num  # Update the current prefix sum
            
            # Check if there's a prefix sum that can form the required sum k
            if (current_sum - k) in prefix_sum_count:
                result += prefix_sum_count[current_sum - k]
            
            # Update the count of the current prefix sum in the hash map
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1
        
        return result