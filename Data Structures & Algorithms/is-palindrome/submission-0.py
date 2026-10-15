class Solution:
    def isPalindrome(self, s: str) -> bool:
        listForward = []
        for c in s:
            if c.isalnum():
                listForward.append(c.upper())
        listBackward = listForward.copy()
        listBackward.reverse()
        if listBackward == listForward:
            return True       
        return False