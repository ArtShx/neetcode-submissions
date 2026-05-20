class Solution:
    key = "__#__"

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            out.append(self.key)
            out.append(s)
        return "".join(out)

    def decode(self, s: str) -> List[str]:
        return s.split(self.key)[1:]
