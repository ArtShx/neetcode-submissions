class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        word_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            #print(word, sorted_word)
            if sorted_word not in word_map:
                word_map[sorted_word] = []
            word_map[sorted_word].append(word)

        for sortedword, words in word_map.items():
            res.append(words)
        return res