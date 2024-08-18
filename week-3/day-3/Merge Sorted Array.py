class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Start from the end of nums1 and nums2
        p1 = m - 1  # Last element of the non-zero part of nums1
        p2 = n - 1  # Last element of nums2
        p = m + n - 1  # Last position in nums1

        # While there are elements to compare in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are still elements left in nums2, copy them
        # (no need to copy elements from nums1 as they are already in place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
