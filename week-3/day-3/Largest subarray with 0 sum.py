class Solution:
    def maxLen(self, n, arr):
        # Dictionary to store the sum and its corresponding index
        sum_index_map = {}
        max_length = 0
        current_sum = 0
        
        for i in range(n):
            # Add the current element to the sum
            current_sum += arr[i]
            
            if current_sum == 0:
                max_length = i + 1
            
            # If sum is already seen, calculate the length of the subarray
            if current_sum in sum_index_map:
                max_length = max(max_length, i - sum_index_map[current_sum])
            else:
                # Store this sum with index if not seen before
                sum_index_map[current_sum] = i
        
        return max_length
