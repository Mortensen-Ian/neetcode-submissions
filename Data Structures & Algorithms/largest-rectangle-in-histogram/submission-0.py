class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ## For every index I want to determine the width of a rectangle
        ## with that height.
        rBound = dict()
        lBound = dict()
        stack1 = []
        stack2 = []
        for i in range(len(heights)):
            while stack1 and heights[i] < heights[stack1[-1]]:
                ind1 = stack1.pop()
                rBound[ind1] = i
            while stack2 and heights[len(heights)-i-1] < heights[stack2[-1]]:
                ind2 = stack2.pop()
                lBound[ind2] = len(heights)-i
            stack1.append(i)
            stack2.append(len(heights)-i-1)
        while stack1:
            rBound[stack1.pop()] = len(heights)
        while stack2:
            lBound[stack2.pop()] = 0
        m = 0
        for i in range(len(heights)):
            m = max(m, (rBound[i]-lBound[i]) * heights[i])
        return m
            
