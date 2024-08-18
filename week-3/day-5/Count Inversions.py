class Solution:
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Helper function to merge two halves and count inversions
        def merge_and_count(arr, temp_arr, left, mid, right):
            i = left    # Starting index for left subarray
            j = mid + 1 # Starting index for right subarray
            k = left    # Starting index to be sorted
            inv_count = 0

            # Process both subarrays and count inversions
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    temp_arr[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            # Copy the remaining elements of left subarray, if any
            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1

            # Copy the remaining elements of right subarray, if any
            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1

            # Copy the sorted subarray into the original array
            for i in range(left, right + 1):
                arr[i] = temp_arr[i]
                
            return inv_count

        # Helper function to implement merge sort and count inversions
        def merge_sort_and_count(arr, temp_arr, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
                inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

                inv_count += merge_and_count(arr, temp_arr, left, mid, right)

            return inv_count

        # Initializing the temporary array
        temp_arr = [0] * n
        return merge_sort_and_count(arr, temp_arr, 0, n - 1)

# Example Usage
solution = Solution()
arr = [2, 4, 1, 3, 5]
n = len(arr)