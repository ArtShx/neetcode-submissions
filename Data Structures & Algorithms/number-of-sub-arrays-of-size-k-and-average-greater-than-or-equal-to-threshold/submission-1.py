class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = k-1
        n = len(arr)
        total = sum(arr[:k])
        res = 0

        while i < n:
            
            if i != k-1:
                #print("total=", total, "-", arr[i-k], "+", arr[i], "=", end="")
                total -= arr[i-k]
                total += arr[i]
                #print(total)
                
            average = total / k
            if average >= threshold:
                res += 1
                #print(i)
            i += 1
        return res
            
