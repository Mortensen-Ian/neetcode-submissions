class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = dict()      
        m = 1
        charMax = s[0]
        left = 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            if d[s[i]] > d[charMax]:
                charMax = s[i]
            while i - left + 1 - d[charMax] > k:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    d.pop(s[left])
                left += 1
                charMax = max(d, key=d.get)
            m = max(m, i - left + 1)
        return m
