class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        minimum = prices[0]
        for p in prices:
            m = max(m, p - minimum)
            minimum = min(p, minimum)
        return m
        