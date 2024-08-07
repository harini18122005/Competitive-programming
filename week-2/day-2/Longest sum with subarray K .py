class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        # Dictionary to store the sum of elements up to each index
        sum_map = {}
        current_sum = 0
        max_length = 0
        
        # Traverse through the array
        for i in range(n):
            current_sum += arr[i]
            
            # Check if current_sum is equal to k
            if current_sum == k:
                max_length = i + 1
            
            # Check if (current_sum - k) is present in sum_map
            if (current_sum - k) in sum_map:
                max_length = max(max_length, i - sum_map[current_sum - k])
            
            # Store the first occurrence of current_sum in sum_map
            if current_sum not in sum_map:
                sum_map[current_sum] = i
        
        return max_length
