class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for letter in s:
            if letter in pairs:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != pairs[letter]:
                    return False
            else:      
                stack.append(letter)
        return len(stack) == 0