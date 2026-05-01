class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(index: int, arr: List[int]):
            #print(arr, index)
            if index == len(nums):
                subsets.append(list(arr))
                return
            
            arr.append(nums[index])
            backtrack(index+1, arr)

            arr.pop()
            backtrack(index+1, arr)
            
        backtrack(0, [])
        return subsets