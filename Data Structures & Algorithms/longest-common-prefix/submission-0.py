class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference = strs[0]
        if not reference:
            return ""

        out = []
        repeat = True
        for i, letter in enumerate(reference):
            if repeat:
                for word in strs:
                    if len(word) <= i or word[i] != letter:
                        repeat = False
                        break
                else:
                    out.append(letter)
        return "".join(out)