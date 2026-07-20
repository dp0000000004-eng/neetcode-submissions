class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for l in s:
            if l in "{([":
                stack.append(l)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if l == ")" and top != "(":
                    return False
                if l == "}" and top != "{":
                    return False
                if l == "]" and top != "[":
                    return False
        
        return not stack

