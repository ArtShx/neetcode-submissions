class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        length = len(mat)
        for i in range(length):
            a = mat[i][i]
            b = mat[i][length-i-1]
            total += a + b
            if i == length-i-1:
                total -= b
        return total