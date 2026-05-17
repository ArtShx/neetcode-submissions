class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        n = len(s)
        m = len(t)

        while j < m and i < n:
            if t[j] == s[i]:
                j += 1
            i += 1
                
        if j == m: # already a subsequence
            return 0

        return m - j
