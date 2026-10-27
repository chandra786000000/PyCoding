class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                # Array is ascending on mid's left side
                if nums[start] <= target <=nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                # Array is ascending on mid's right
                if nums[end] >= target >= nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        return -1