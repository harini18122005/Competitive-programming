class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        
        # Phase 1: Find potential candidates
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Phase 2: Verify candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3 and candidate2 != candidate1:
            result.append(candidate2)
        
        return result