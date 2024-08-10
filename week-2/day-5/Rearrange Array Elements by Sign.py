class Solution(object):
    def rearrangeArray(self, nums):
        # Separate the positive and negative numbers
        positive_nums = [num for num in nums if num > 0]
        negative_nums = [num for num in nums if num < 0]

        # Interleave the positive and negative numbers
        result = []
        for i in range(len(positive_nums)):
            result.append(positive_nums[i])
            result.append(negative_nums[i])

        return result

