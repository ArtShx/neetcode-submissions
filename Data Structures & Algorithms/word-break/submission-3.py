class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        cache = set()
        def helper(curword: str):
            #print(f"{curword=}")
            if curword == "":
                return True
            if curword in cache:
                #print("\tLEFT2")
                return False
            for word in wordDict:
                #if word in curword.startswith(word) or curword.endswith(word):
                if curword.startswith(word):
                    if helper(curword[len(word):]):
                        return True
                    
                if curword.endswith(word):
                    if helper(curword[:-len(word)]):
                        return True
                    #tmp = curword.replace(word, "")
                    #print(f"\t{curword=} {word=} >>> {tmp=}")
                    #if helper(tmp):
                    #    return True
            
            cache.add(curword)
            #print("\tLEFT1")
            return False
        
        out = helper(s)
        #print(cache)
        return out
            