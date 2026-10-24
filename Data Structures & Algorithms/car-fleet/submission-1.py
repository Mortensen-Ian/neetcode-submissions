class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(speed)):
            speed[i] = (target - position[i]) / speed[i]
        
        speed = [speed for _, speed in sorted(zip(position, speed))]
        m = 0
        total = 0
        for t in reversed(speed):
            if t > m:
                total += 1
                m = t
        return total
        