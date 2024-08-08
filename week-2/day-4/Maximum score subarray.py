class Solution:
    def pairWithMaxSum(self, arr):
        n = len(arr)
        max_score = 0

        for i in range(n):
            for j in range(i + 1, n):
                subarray = arr[i:j + 1]
                if len(subarray) < 2:
                    continue

                min1, min2 = float('inf'), float('inf')
                for num in subarray:
                    if num < min1:
                        min2 = min1
                        min1 = num
                    elif num < min2:
                        min2 = num

                score = min1 + min2
                max_score = max(max_score, score)

        return max_score


