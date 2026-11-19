class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            diff = heapq.heappop_max(stones) - heapq.heappop_max(stones)
            if diff > 0:
                heapq.heappush_max(stones, diff)
        if len(stones) == 0:
            return 0
        return stones[0]