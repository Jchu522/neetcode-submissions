class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # there is always at least 1 gas station
        # if the circuit is impossible return -1
        # there is only 1 unique answer
        cur = 0
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            
            if cur < 0:
                cur = 0
                start = i + 1
        
        if total < 0:
            return -1
            
        else:
            return start



        