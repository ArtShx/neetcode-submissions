class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_chars = {}
        ransom_chars = {}
        for char in magazine:
            if char not in magazine_chars:
                magazine_chars[char] = 0
            magazine_chars[char] += 1
        
        for char in ransomNote:
            if char not in magazine_chars:
                return False
            if magazine_chars[char] == 0:
                return False
            magazine_chars[char] -= 1
        return True
        

