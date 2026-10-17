class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        m = 0
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
                d[s[i]] = i
            else:
                d[s[i]] = i
                m = max(m, i - start + 1)
        return m