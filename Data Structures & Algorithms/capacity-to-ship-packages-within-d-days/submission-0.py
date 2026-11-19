class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ret = r

        while r >= l:
            mid = (l + r ) // 2
            day = 1
            temp = mid
            for weight in weights:
                if temp - weight < 0:
                    temp = mid
                    day += 1
                temp -= weight
            
            if day <= days:
                ret = min(ret, mid)
                r = mid - 1
            elif day > days:
                l = mid + 1

        return ret

