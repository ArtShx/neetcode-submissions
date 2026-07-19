class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        n = len(nums)
        threshold = n/3
        res = set()

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
            if counter[num] > threshold:
                res.add(num)
        return list(res)
