class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr

        dist = [0 for i in range(len(arr))]
        for i, val in enumerate(arr):
            dist[i] = abs(val - x)


        l = 0
        r = k - 1

        minSoFar = sum(dist[:k])
        curr = minSoFar
        res = arr[:k]

        while r + 1 < len(arr):
            r += 1
            curr += dist[r]

            if r - l + 1 > k:
                curr -= dist[l]
                l += 1

            if curr < minSoFar:
                res = arr[l:r+1]
                minSoFar = curr

        return res


                

            
                

