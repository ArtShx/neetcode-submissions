class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        letters = defaultdict(int)
        for word in words:
            for letter in word:
                letters[letter] += 1
        if len(set(letters.values())) != 1:
            return False
        
        # 3a 3b 3c
        word_letters = defaultdict(int)
        for letter, counter in letters.items():
            if not (counter / len(words)).is_integer():
                return False
            #word_letters[letter] = counter / len(words)
        #print(word_letters)
        return True

        required_letters = list(letters.keys())
        for word in words:
            for letter in word:
                if letter not in letters:
                    return False
                letters[letter] -= 1
                if letters[letter] == 0:
                    del letters[letter]
            if len(set(letters.values())) != 1:
                return False
            if len(set(letters.keys())) != len(required_letters):
                return False
        return True