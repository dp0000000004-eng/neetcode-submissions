class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        
        for i in range(len(operations)):
            token = operations[i]
            
            try:
                val = int(token)
                stack.append(val)
            except ValueError:
                if token == "C":
                    if stack:
                        stack.pop()
                elif token == "D":
                    if stack:
                        stack.append(stack[-1] * 2)
                elif token == "+":
                    if len(stack) >= 2:
                        stack.append(stack[-1] + stack[-2])
                else:
                    continue

        return sum(stack)