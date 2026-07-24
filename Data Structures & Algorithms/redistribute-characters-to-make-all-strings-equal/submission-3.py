class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        letters = defaultdict(int)
        for word in words:
            for letter in word:
                letters[letter] += 1
    
        word_letters = defaultdict(int)
        for letter, counter in letters.items():
            if not (counter / len(words)).is_integer():
                return False

        return True
