class Solution:
    def insert(self, arr, n):
        
        key = arr[n]
        j = n - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    def insertionSort(self, arr, n):
        for i in range(1, n):
            self.insert(arr, i)


if __name__ == "__main__":
    arr = [4, 1, 3, 9, 7]
    n = len(arr)
    ob = Solution()
    ob.insertionSort(arr, n)
    print(arr)  