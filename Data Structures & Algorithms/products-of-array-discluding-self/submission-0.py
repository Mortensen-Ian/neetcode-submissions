class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = dict()
        right = dict()
        leftProd = 1
        rightProd = 1
        for i in range(len(nums)):
            left[i] = leftProd
            right[len(nums)-i-1] = rightProd
            leftProd  = leftProd * nums[i]
            rightProd = rightProd* nums[len(nums)-i-1]
        numProducts = []
        for i in range(len(nums)):
            numProducts.append(left[i] * right[i])
        return numProducts

        