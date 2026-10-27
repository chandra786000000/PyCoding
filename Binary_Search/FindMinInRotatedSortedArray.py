class Solution:
    def findMin(self, nums: list[int]) -> int:
        start, end = 0, len(nums)-1
        lowest = nums[0]
        while(start<=end):
            mid = (start+end)//2
            print(start, mid, end)
            lowest = min(lowest , nums[mid])
            if nums[mid] < nums[start]:
                end = mid-1
            elif nums[mid] > nums[end]:
                start = mid+1
            else: # this is the case when array between start -> end is ascending 
                return min(lowest,nums[start])
        return lowest