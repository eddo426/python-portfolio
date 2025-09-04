class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 1 or len(s) > 10**4:
            return None
        validChars = {')': '(', ']': '[', '}': '{'}
        stack = []
        for a in s:
            if a in validChars:
                top = stack.pop() if stack else 'f'
                if validChars[a] != top:
                    return False
            else:
                stack.append(a)
        return not stack