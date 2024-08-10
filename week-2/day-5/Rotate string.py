class Solution(object):
    def rotateString(self, s, goal):
        # Check if lengths are the same
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself
        doubled_s = s + s
        
        # Check if goal is a substring of the concatenated string
        return goal in doubled_s

