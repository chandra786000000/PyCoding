class Solution:
    def rob(self, nums: List[int]) -> int:
        n  = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            if i<3:
                dp[i] = nums[i-1]
            else:
                dp[i] = max(nums[i-1]+dp[i-2],nums[i-1]+dp[i-3])
        return max(dp[n],dp[n-1])
        