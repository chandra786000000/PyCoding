class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: # type: ignore
        n = len(nums)
        if n<1:
            return 0
        dp = [ 1 for _ in range(n)]
        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        
        return max(dp)

# dp[i] =  length of lis including i as the last element)