class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        ans = 0
        for i in numSet:
            if i - 1 not in numSet:
                n = i
                sum_till_now = 0
                while n in numSet:
                    sum_till_now += 1
                    n += 1
                ans = max(ans, sum_till_now)
        return ans