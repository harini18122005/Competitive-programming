class Solution:
    def isIsomorphic(self, s, t):
        # Maps to keep track of character mappings from s to t and t to s
        s_to_t = {}
        t_to_s = {}

        # Iterate over characters in s and t
        for char_s, char_t in zip(s, t):
            # Check if char_s is already mapped
            if char_s in s_to_t:
                # If mapped character does not match char_t, return False
                if s_to_t[char_s] != char_t:
                    return False
            else:
                # Map char_s to char_t
                s_to_t[char_s] = char_t

            # Check if char_t is already mapped
            if char_t in t_to_s:
                # If mapped character does not match char_s, return False
                if t_to_s[char_t] != char_s:
                    return False
            else:
                # Map char_t to char_s
                t_to_s[char_t] = char_s

        return True
