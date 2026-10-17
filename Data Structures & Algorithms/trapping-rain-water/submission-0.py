class Solution:
    def trap(self, height: List[int]) -> int:
        maxInd = 0
        total = 0
        s = 0
        for i in range(1,len(height)):
            if height[i] >=  height[maxInd]:
                total += self.calcBasin(height, maxInd, i, s)
                maxInd = i
                s = 0
            else:
                s += height[i]
        
        rightMax = len(height) -1
        s = 0
        for i in reversed(range(maxInd, len(height)-1)):
            if height[i] > height[rightMax]:
                total += self.calcBasin(height, i, rightMax, s)
                rightMax = i
                s = 0
            else:
                s += height[i]
        
        return total

    def calcBasin(self, height, start, stop, subtract):
        length = stop - start -1
        minHeight = min(height[start], height[stop])
        return max(0, (length * minHeight) - subtract)