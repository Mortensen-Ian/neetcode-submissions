class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        q = deque()
        values = list(d.values())
        heapq.heapify_max(values)
        t = 0
        while values or q:
            t += 1
            if not values:
                ## Move time to t and then pop off queue.
                t = max(q[0][1] + 1, t)
                v = q.popleft()[0] - 1
                if v > 0:
                    q.append((v, t + n))
            else:
                ## Pop off values and push on to queue
                if q and q[0][1] < t:
                    heapq.heappush_max(values, q.popleft()[0])
                v = heapq.heappop_max(values) - 1
                if v > 0:
                    q.append((v, t + n))
        return t

