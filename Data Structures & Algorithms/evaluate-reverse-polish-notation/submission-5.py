class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)  # b - a not a - b
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":  # fixed from "-" to "/"
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  # b / a with int truncation toward zero
            else:
                stack.append(int(c))
        return stack[0]