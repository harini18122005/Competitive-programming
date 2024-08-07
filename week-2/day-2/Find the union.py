class Solution:
    def findUnion(self, arr1, arr2, n, m):
        set1 = set(arr1)
        set2 = set(arr2)
        union_set = set1.union(set2)
        result = sorted(union_set)
        
        return result
