class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        k +=1
        nums.append(1001)
        l = min(len(nums),k)
        nums.sort(reverse=True)
        nums = nums[:l]
        heapq.heapify(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif self.nums[0] < val:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]
