class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            point.append(distance)
        points.sort(key=lambda z: z[2])
        for i in range(k):
            points[i].pop()
        return points[:k]