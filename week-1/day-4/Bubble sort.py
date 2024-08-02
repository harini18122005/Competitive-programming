class Solution:
    def bubbleSort(self, arr, n):
        
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    arr = [4, 1, 3, 9, 7]
    n = len(arr)
    ob = Solution()
    ob.bubbleSort(arr, n)  
    print(arr)  
