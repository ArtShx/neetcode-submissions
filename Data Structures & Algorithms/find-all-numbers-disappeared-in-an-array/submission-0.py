class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mynum = set([x for x in range(1, n+1)])
        for num in nums:
            if num in mynum:
                mynum.remove(num)
        return list(mynum)