class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret = {}
        indexs = []
        for i in range(len(s)):
            ret[s[i]] = i
        curr = 0
        prev = 0
        for i, char in enumerate(s):
            
            curr = max(curr, ret[char])
            if curr == i:

                indexs.append(i+1 - prev)
                prev = i + 1
            
        
        return indexs
