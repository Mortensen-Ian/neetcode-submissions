class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif t == "-":
                stack.append(-int(stack.pop()) + int(stack.pop()))
            elif t == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif t == "/":
                divisor = int(stack.pop())
                if divisor == 0:
                    stack.append(0)
                else:
                    stack.append(int(stack.pop()) / divisor)  
            else:
                stack.append(t) 
        return int(stack[0])
        