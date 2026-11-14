class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = {chr(i): 0 for i in range(ord('a'), ord('z')+ 1)}
        s2Count = {chr(i): 0 for i in range(ord('a'), ord('z')+ 1)}
        
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
        match = 0 

        for key in s1Count:
            match += 1 if s1Count[key] == s2Count[key] else 0 
            if match == 26:
                return True

        l = 0 
        # add and remove 1 from r and l
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True
            key = s2[r]
            keyl = s2[l]
            s2Count[key] +=1
            if s2Count[key] == s1Count[key]:
                match += 1
            if s2Count[key] == s1Count[key] + 1:
                match -= 1

            s2Count[keyl] -=1
            if s2Count[keyl] == s1Count[keyl]:
                match += 1
            if s2Count[keyl] == s1Count[keyl] - 1:
                match -= 1


            l += 1
        if match == 26:
            return True


        return False

