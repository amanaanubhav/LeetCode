class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            #condition
            if e in '({[':
                stack.append(e)
            else:
                # Handle empty stack crash
                if not stack:
                    return False
                
                # Check for match and use pop()
                if e == ')' and stack[-1] == '(':
                    stack.pop()
                elif e == '}' and stack[-1] == '{':
                    stack.pop()
                elif e == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        return not stack
