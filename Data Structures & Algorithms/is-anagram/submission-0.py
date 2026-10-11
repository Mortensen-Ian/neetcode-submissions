class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()
        for l in s:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
        for l in t:
            if l in letters:
                letters[l] -= 1
            else:
                return False
        for value in letters.values():
            if value != 0:
                return False
        return True
        
        