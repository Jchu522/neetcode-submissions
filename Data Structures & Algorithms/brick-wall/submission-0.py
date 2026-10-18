class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # for w in wall:
        #     print(w)

        # gaps = [[] for i in range(len(wall))]
        freq = {}
        width = sum(wall[0])

        for row in range(len(wall)):
            dist = 0
            for brick in wall[row]:
                dist += brick
                freq[dist] = freq.get(dist, 0) + 1
                # gaps[row].append(dist)
            # gaps[row] = gaps[row][:-1]
        del freq[width]
        # print(freq)
        if not freq:
            return len(wall)

        return len(wall)-max(freq.values())



