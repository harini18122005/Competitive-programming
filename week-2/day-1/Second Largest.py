class Solution:
    def print2largest(self, arr):
        first_largest = float('-inf')
        second_largest = float('-inf')
        
        for num in arr:
            if num > first_largest:
                second_largest = first_largest
                first_largest = num
            elif num > second_largest and num != first_largest:
                second_largest = num
        if second_largest == float('-inf'):
            return -1
        else:
            return second_largest