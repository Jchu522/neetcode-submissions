class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        ret = 0
        l = 0
        r = 0
        temp = 0
        while r < len(fruits):
            
            ret = max(temp, ret)
            if fruits[r] not in baskets:
                baskets[fruits[r]] = 1
            else:
                baskets[fruits[r]] += 1
            temp +=1
            
            while len(baskets) > 2:
                    temp -= 1
                    baskets[fruits[l]] -= 1
                    if baskets[fruits[l]] == 0:
                        baskets.pop(fruits[l])
                    l += 1
            r += 1

        ret = max(temp,ret)

        return ret

