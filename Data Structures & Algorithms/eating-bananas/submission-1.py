class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)   
        highest = right
        while left <= right:
            r = left + (right - left) // 2
            canEatPile = self.canEatPiles(piles, r, h)
            if not canEatPile:
                left = r + 1
            else:
                highest = r
                right = r - 1
                
        return highest            


    def canEatPiles(self, piles, r, h):
        t = 0
        for p in piles:
            t += (p + r - 1) // r
            if t > h:
                return False
        return True