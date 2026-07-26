class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        n = len(firstList)
        m = len(secondList)
        out = []
        while i < n and j < m:
            #print(i, j)
            first = firstList[i]
            second = secondList[j]
            if (first[0] <= second[1] and second[0] <= first[1]) or \
                    (second[0] <= first[1] and first[0] <= second[1]):
                print("merge")
                out.append([max(first[0], second[0]), min(first[1], second[1])])
            if max(first) <= max(second):
                i+=1
            else:
                j+=1
        return out