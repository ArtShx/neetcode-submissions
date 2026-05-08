class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == "+":
                new = stack[-1] + stack[-2]
                stack.append(new)
                res += new
            elif op == "C":
                n = stack.pop()
                res -= n

            elif op == "D":
                new = stack[-1] * 2
                stack.append(new)
                res += new
            else:
                n = int(op)
                stack.append(n)
                res += n
        return res