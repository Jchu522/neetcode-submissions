class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newarr = nums1 + nums2
        newarr.sort()
        n = len(newarr)
        if n % 2 == 1:
            return newarr[ n // 2 ]
        else:
            return (newarr[n//2] + newarr[n//2 - 1]) /2