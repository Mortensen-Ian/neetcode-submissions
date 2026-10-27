class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        smallest = nums[0]
        while l <= r:
            m = (l + r) // 2
            smallest = min(smallest, nums[m], nums[l])
            if nums[l] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        return smallest
