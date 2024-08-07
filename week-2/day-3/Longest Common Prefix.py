class Solution:
    def longestCommonPrefix(self, strs): 
        if not strs:
            return ""
        
        # Find the minimum length string in the array
        min_length = min(len(s) for s in strs)
        
        # Initialize the longest common prefix as empty
        lcp = ""
        
        # Compare characters at each index
        for i in range(min_length):
            # Take the character from the first string
            char = strs[0][i]
            
            # Check this character against all strings
            for s in strs:
                if s[i] != char:
                    return lcp
            
            # If all strings match, add the character to the prefix
            lcp += char
        
        return lcp

