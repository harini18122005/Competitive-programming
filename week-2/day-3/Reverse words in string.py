class Solution(object):
    def reverseWords(self, s):
        # Step 1: Trim leading and trailing spaces
        s = s.strip()
        
        # Step 2: Split the string into words (handling multiple spaces)
        words = s.split()
        
        # Step 3: Reverse the order of words
        words.reverse()
        
        # Step 4: Join the words with a single space
        reversed_s = ' '.join(words)
        
        return reversed_s


        