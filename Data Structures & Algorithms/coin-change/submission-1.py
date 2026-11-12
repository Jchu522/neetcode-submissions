class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ret = [amount + 1 for i in range(amount + 1)]
        ret[0] = 0
        for i in range(1, amount+1):

            for coin in coins:
                if i - coin >= 0:
                    ret[i] = min(ret[i], ret[i-coin] + 1)
                

        return ret[-1] if ret[-1] <= amount else -1