class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxval = arr[-1]
        out = [-1] * n
        for i in range(n-1, -1, -1):
            out[i] = maxval
            maxval = max(maxval, arr[i])
        out[-1] = -1
        return out