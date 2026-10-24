class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper = len(nums)
        lower = 0
        newInd = (upper + lower)//2 
        while upper - lower > 1 and nums[newInd] != target:
            if nums[newInd] > target:
                upper = newInd
            else:
                lower = newInd
            newInd = (upper + lower)//2
        if nums[newInd] == target:
            return newInd
        return -1
            