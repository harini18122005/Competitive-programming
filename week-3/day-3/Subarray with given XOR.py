class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        xor_map = {}
        xor_sum = 0
        count = 0
        
        for num in A:
            # Calculate the current XOR sum
            xor_sum ^= num
            
            # Check if the current XOR sum equals B
            if xor_sum == B:
                count += 1
            
            # Calculate the required XOR to find in previous results
            required_xor = xor_sum ^ B
            if required_xor in xor_map:
                count += xor_map[required_xor]
            
            # Update the map with the current XOR sum
            if xor_sum in xor_map:
                xor_map[xor_sum] += 1
            else:
                xor_map[xor_sum] = 1
        
        return count
