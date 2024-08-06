class Solution:
    def largest(self, n, arr):
        max_element = arr[0]
        for element in arr[1:]:
            if element > max_element:
                max_element = element

        return max_element

# Example usage:
if __name__ == "__main__":
    n = 5
    arr = [1, 8, 7, 56, 90]
    obj = Solution()
    res = obj.largest(n, arr)
    