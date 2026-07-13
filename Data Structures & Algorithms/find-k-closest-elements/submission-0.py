import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n-1
        out = []
        for num in arr:
            diff = abs(num - x)
            out.append((diff, num))
        
        arr1 = sorted(out, key=lambda ar: ar[0])[:k]
        arr2 = sorted([item[1] for item in arr1])
        
        return arr2
