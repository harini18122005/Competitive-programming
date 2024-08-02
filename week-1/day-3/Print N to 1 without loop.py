class Solution:
    def printNos(self, N):
        if N < 1:
            return
        print(N, end=" ")
        self.printNos(N - 1)

