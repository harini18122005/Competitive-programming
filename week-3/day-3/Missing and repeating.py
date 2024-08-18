
class Solution:
    def findTwoElement(self, arr, n):
        result = [0, 0]
        
        # Step 1: Identify the repeating number
        for i in range(n):
            index = abs(arr[i]) - 1  # Get the index (1-based to 0-based)
            
            # Check if the value at this index is already negative
            if arr[index] < 0:
                result[0] = abs(arr[i])  # This is the repeating number
            else:
                # Mark the value at index as visited by making it negative
                arr[index] = -arr[index]
        
        # Step 2: Identify the missing number
        for i in range(n):
            if arr[i] > 0:
                result[1] = i + 1  # The missing number is index + 1
                break
        
        return result

