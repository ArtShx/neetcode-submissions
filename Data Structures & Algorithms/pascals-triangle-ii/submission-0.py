class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1], [1, 1], [1,2,1]]
        for i in range(3, rowIndex+1):
            #print(i, rows[-1])
            newrow = [1]
            for j in range(1, i):
                #print("\t", j)
                newrow.append(rows[-1][j-1] + rows[-1][j])
            newrow.append(1)
            rows.append(newrow)
        return rows[rowIndex]