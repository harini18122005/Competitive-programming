class Solution:
    def printNos(self, n):
        if n == 1:
            print(1, end=" ")
            return
       
        self.printNos(n - 1)
        print(n, end=" ")
