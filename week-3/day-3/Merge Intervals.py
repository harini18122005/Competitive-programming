class Solution:
    def merge(self, intervals):
        # Step 1: Sort intervals by their starting values
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize the merged list with the first interval
        merged = []
        
        for interval in intervals:
            # If merged is empty or there is no overlap with the last interval in merged
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is overlap, merge the intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
