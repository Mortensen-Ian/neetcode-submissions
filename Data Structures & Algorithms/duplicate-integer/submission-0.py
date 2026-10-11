class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(numSet) == len(nums):
            return False
        return True
