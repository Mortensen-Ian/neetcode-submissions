class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexStorage = dict()
        for i in range(len(nums)):
            if nums[i] in indexStorage:
                indexStorage[nums[i]].append(i)
            else:
                indexStorage[nums[i]] = [i]
        for i in range(len(nums)):
            intToAdd = target - nums[i]
            if intToAdd in indexStorage:
                for index in indexStorage[intToAdd]:
                    if index != i:
                        ReturnedList = [i, index]
                        ReturnedList.sort()
                        return ReturnedList
        return [0, 0]
        