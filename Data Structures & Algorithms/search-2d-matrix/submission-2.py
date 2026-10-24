class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lcol = 0
        rcol = len(matrix[0])
        row = self.GetRow(matrix, target)
        if row == -1:
            return False
        if self.GetColumn(target, matrix[row]) == -1:
            return False
        return True
        
    def GetColumn(self, target, nums):
        l = 0
        r = len(nums)-1
        while l <= r:
            i = l + (r-l)//2
            if nums[i] < target:
                l = i + 1
            elif nums[i] > target:
                r = i - 1
            else:
                return i
        return -1

    def GetRow(self, matrix, target):
        lrow = 0
        rrow = len(matrix)-1
        while lrow <= rrow:
            curRow = lrow + (rrow-lrow)//2  
            if matrix[curRow][0] <= target and matrix[curRow][-1] >= target:
                return curRow 
            elif matrix[curRow][0] >= target:
                rrow = curRow - 1
            else:
                lrow = curRow + 1
        return -1