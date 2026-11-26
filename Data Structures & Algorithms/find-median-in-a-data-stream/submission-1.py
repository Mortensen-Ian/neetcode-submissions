class MedianFinder:

    def __init__(self):
        small = [-100001]
        large = [100001]
        heapq.heapify_max(small)
        heapq.heapify(large)
        self.small = small
        self.large = large

    def addNum(self, num: int) -> None:
        if num <= self.small[0]:
            heapq.heappush_max(self.small, num)
            if len(self.small) > len(self.large) + 1:
                heapq.heappush(self.large, heapq.heappop_max(self.small))
        else:
            heapq.heappush(self.large, num)
            if len(self.large) > len(self.small):
                heapq.heappush_max(self.small, heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.small[0] + self.large[0])/2
        else:
            return self.small[0]
