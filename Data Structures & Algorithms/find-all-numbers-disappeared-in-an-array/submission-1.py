class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mynum = set([x for x in range(1, n+1)])
        for num in nums:
            mynum.discard(num)
        return list(mynum)