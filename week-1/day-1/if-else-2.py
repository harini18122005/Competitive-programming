class Solution:
    def compareNM(self, n: int, m: int) -> str:
        if n < m:
            return 'lesser'
        elif n == m:
            return 'equal'
        else:
            return 'greater'


obj = Solution()
res = obj.compareNM(4, 8) 