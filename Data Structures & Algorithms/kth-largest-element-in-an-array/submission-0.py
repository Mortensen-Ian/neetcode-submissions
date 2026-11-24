class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)
        for num in nums:            
            heapq.heappush(h, num)
            k -= 1
            if k < 0:
                k += 1
                heapq.heappop(h)
        return h[0]