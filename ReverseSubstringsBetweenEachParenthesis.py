class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        p = {}
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                j = stack.pop()
                p[i] = j
                p[j] = i
        i = 0
        d = 1 
        result = []
        while i < len(s):
            if s[i] in "()":
                i = p[i]   
                d = -d        
            else:
                result.append(s[i])
            i += d
        return "".join(result)
