class Solution:
    def longestConsecutive(self, nums):
        # Convert the list to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if it is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count the length of the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak found
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
