class Solution:
    def returnSum(self,n) -> int:
        ans = 0
        while n>0:
            last = n%10
            ans += last*last
            n //=10
        return ans

    def isHappy(self, n: int) -> bool:
        numMap = {}
        while n not in numMap:
            if n == 1:
                return True
            numMap[n] = 1
            n = self.returnSum(n)
        return False
