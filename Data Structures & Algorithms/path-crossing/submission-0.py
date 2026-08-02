class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visits = set()
        r, c = [0, 0]
        visits.add((r, c))
        deltamap = {
            "N": [1, 0],
            "S": [-1, 0],
            "E": [0, 1],
            "W": [0, -1]
        }
        for dir in path:
            rd, cd = deltamap[dir]
            r += rd
            c += cd
            if (r, c) in visits:
                return True
            visits.add((r, c))
        return False

