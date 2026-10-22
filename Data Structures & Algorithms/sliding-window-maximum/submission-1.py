class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curMax = -1
        maxes = []
        for i in range(k - 1, len(nums)):
            lowerBound = i - k + 1
            if curMax < lowerBound:
                curMax = lowerBound
                for j in range(lowerBound, i + 1):
                    if nums[j] >= nums[curMax]:
                        curMax = j
            else:
                if nums[i] >= nums[curMax]:
                    curMax = i
            maxes.append(nums[curMax])
        return maxes
        