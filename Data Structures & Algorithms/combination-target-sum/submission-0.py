class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(total: int, arr: List[int], index: int):
            if total == target:
                print(total, target, arr)
                res.append(list(arr))
                return

            if total > target:
                return
            if index == len(nums):
                return

            arr.append(nums[index])
            backtrack(total + nums[index], arr, index)

            arr.pop()
            #backtrack(total, arr, index)

            backtrack(total, arr, index+1)
        
        backtrack(0, [], 0)
        return res