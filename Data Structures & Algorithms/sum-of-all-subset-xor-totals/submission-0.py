class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        subsets = get_subsets(nums)
        print(subsets)
        total = 0

        for arr in subsets:
            xor = calc_xor(arr)
            total += xor
            print(arr, xor)
        return total


def get_subsets(arr: List[int]) -> List[List[int]]:
    out = []
    def backtrack(index, path):
        if index == len(arr):
            out.append(list(path))
            return out
        
        # path 1
        path.append(arr[index])
        backtrack(index+1, path)

        # path 2
        path.pop()
        backtrack(index+1, path)
    
    backtrack(0, [])
    return out


def calc_xor(arr: List[int]) -> int:
    out = 0
    for num in arr:
        out ^= num
    return out