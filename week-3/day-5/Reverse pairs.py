class Solution:
    def reversePairs(self, nums):
        # Helper function to merge and count reverse pairs
        def merge_and_count(nums, left, mid, right):
            count = 0
            j = mid + 1
            # Count reverse pairs
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            # Merge step of merge sort
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
            
            while j <= right:
                temp.append(nums[j])
                j += 1
            
            # Copy the sorted elements back into original array
            for i in range(left, right + 1):
                nums[i] = temp[i - left]
            
            return count
        
        # Helper function to implement merge sort and count reverse pairs
        def merge_sort_and_count(nums, left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_sort_and_count(nums, left, mid)
            count += merge_sort_and_count(nums, mid + 1, right)
            count += merge_and_count(nums, left, mid, right)
            return count
        
        return merge_sort_and_count(nums, 0, len(nums) - 1)


