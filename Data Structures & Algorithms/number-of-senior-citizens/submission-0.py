class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0
        for det in details:
            age = int(det[11:13])
            if age > 60:
                total+=1
        return total