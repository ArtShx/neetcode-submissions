class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        strn = str(x)
        for i in range(len(strn)):
            if strn[i] != strn[-i-1]:
                return False
        return True