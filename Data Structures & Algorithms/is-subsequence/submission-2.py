class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        while i < len(s):
            if s[i] == t[j]:
                i+=1
                if i == len(s):
                    return True
            j+=1
            if j == len(t):
                return False
        return False
            