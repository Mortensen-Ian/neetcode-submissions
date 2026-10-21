class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = dict()
        for c in t:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        substring = s + t
        left = 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] -= 1
                while max(d.values()) <= 0:
                    if i - left + 1 < len(substring):
                        substring = s[left:i+1]
                    if s[left] in d:
                        d[s[left]] += 1
                    left += 1
        if substring == s + t:
            return ""
        return substring
