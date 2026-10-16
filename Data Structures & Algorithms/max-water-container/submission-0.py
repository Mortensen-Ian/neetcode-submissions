class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        lmax = 0
        rmax = len(heights) -1
        lind = 0
        rind = len(heights)-1
        while lind < rind:
            if heights[lind] > heights[lmax]:
                lmax = lind
            if heights[rind] > heights[rmax]:
                rmax = rind
            m = max(m, min(heights[lmax], heights[rmax]) * (rmax - lmax))
            if heights[lind] > heights[rind]:
                rind -= 1
            else:
                lind += 1
        return m
            
    
    #7, 8, 1, 1 20, 10, 10