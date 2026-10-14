class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        maximum = 1
        cur = 1
        for i in range(len(nums)-1):
            sequential = (nums[i] + 1 == nums[i+1])
            equal = (nums[i] == nums[i+1])
            if sequential:
                cur += 1    
            if cur > maximum:
                maximum = cur
            if not sequential and not equal:
                cur = 1
        return maximum
            
#[0,3,2,5,4,6,1,1]
#[0, 1, 1, 2, 3, 4, 5, 6]
        #[2, 3, 5, 7, 8, 9]

        