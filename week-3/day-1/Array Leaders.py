class Solution:
    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        # Initialize an empty list to store leaders
        leaders = []
        
        # Start with the rightmost element as the current maximum
        max_from_right = arr[-1]
        
        # The rightmost element is always a leader
        leaders.append(max_from_right)
        
        # Traverse the array from right to left starting from second last element
        for i in range(n-2, -1, -1):
            if arr[i] >= max_from_right:
                leaders.append(arr[i])
                max_from_right = arr[i]
        
        # Since we collected leaders in reverse order, reverse the list before returning
        leaders.reverse()
        
        return leaders

