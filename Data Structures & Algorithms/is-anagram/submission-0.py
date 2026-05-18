class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
        
        for char in t:
            if counter.get(char, 0) == 0:
                return False
            if counter[char] == 1:
                del counter[char]
            else:
                counter[char] -= 1
        return not bool(counter)
        