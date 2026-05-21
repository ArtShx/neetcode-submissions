class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1

        while l < r:
            if not s[l].isalnum() or s[l] == " ":
                l += 1
                continue
            if not s[r].isalnum() or s[r] == " ":
                r -= 1
                continue
            #print(l, r, s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
