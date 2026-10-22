class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in d:
                stack.append(c)
            elif stack == [] or d[stack.pop()] != c:
                return False
        return stack == []