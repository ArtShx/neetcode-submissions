class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        res = []
        for pnum, nnum in zip(pos, neg):
            res.extend([pnum, nnum])

        return res