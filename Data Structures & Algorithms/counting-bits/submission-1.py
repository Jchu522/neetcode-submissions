class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n+1)]
        bit = 1

        for i in range(1,n+1):
            if bit * 2 == i:
                bit*=2

            dp[i] = 1 + dp[i-bit] 

        return dp