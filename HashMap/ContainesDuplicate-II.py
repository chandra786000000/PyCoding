class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        map1 = {}
        for i in range(len(nums)):
            if nums[i] in map1:
                if abs(i-map1[nums[i]]) <=k:
                    return True
                map1[nums[i]] = i
            else:
                map1[nums[i]] = i
        return False
