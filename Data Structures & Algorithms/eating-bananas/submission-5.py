class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while r >= l:
            mid = (l + r) // 2
            temp = h
            for p in piles:
                temp -= math.ceil(p / mid)
            if temp >= 0:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res







        
        