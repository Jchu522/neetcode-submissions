class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1 
        ret = 0
        while r >= l:            
            if people[l] + people[r] <= limit:
                ret +=1
                l += 1
                r -= 1 
            else:
                ret +=1
                r -= 1
           
                
        return ret 



