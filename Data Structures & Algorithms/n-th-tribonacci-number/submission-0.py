class Solution:
    def tribonacci(self, n: int) -> int:
        t1 = 0
        t2 = 1
        t3 = 1
        if n == 0:
            return 0
        elif n == 2 or n == 1:
            return 1
        for i in range(n-2):
            tn = t1 + t2 + t3
            t1 = t2
            t2 = t3
            t3 = tn
        return tn