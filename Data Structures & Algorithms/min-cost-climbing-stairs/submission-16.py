class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        ret = [0 for _ in range(len(cost))]
        ret[0] = cost[0]
        ret[1] = cost[1]
        for i in range(2, len(cost)-1):
            ret[i] = min(ret[i-1], ret[i-2]) + cost[i]
            print(ret)

        return min(ret[-2], ret[-3]+ cost[-1])

