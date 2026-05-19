class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
        
        out = sorted(list(counter.items()), key=lambda x: x[1])
        res = []
        for i in range(1, k+1):
            res.append(out[-i][0])
        return res