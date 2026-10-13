class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0 for _ in range(len(arr))]
        Max = -1
        for i in range(len(arr)-1,-1, -1):
            if i == len(arr)-1:
                Max = arr[i]
                arr[i] = -1
                continue
            if Max < arr[i]:
                temp = Max
                Max = arr[i]
                arr[i] = temp
            else:
                arr[i] = Max
        return arr

                
        

