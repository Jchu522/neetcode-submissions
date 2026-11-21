import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        car = []
        for cur in position:
            car.append([cur])

        for i, fast in enumerate(speed):
            car[i].append(fast)
        
        car.sort(key=lambda x:x[0], reverse=True)
        ret = 0
        slowest = 0.0
        for dist, fast in car:
            temp = ((target - dist) / fast)
            if temp > slowest:
                ret += 1
                slowest = temp

        
        return ret

