class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = set()
        real = []
        for i in words:
            for j in words:
                if j == i:
                    continue
                if len(j) < len(i):
                    if j in i and j not in ret:
                        ret.add(j)
                        real.append(j)
        return real
