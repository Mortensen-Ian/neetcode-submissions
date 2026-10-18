class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Build dictionary of letters
        d = dict()
        for c in s1:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in s2:
            if c not in d:
                d[c] = 0

        # Sliding window over s2
        left = 0
        for i in range(len(s2)):
            d[s2[i]] -= 1
            while d[s2[i]] < 0:
                d[s2[left]] += 1
                left += 1
            if i - left + 1 == len(s1):
                return True
                
        print(d)
        return False