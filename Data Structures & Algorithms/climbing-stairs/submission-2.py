class Solution:
    def climbStairs(self, n: int) -> int:
        # arr = [0 for i in range(n + 1)]
        # if n == 1:
        #     return 1
        # arr[1] , arr [2] = 1, 2 
        # for i in range(3, n + 1):
        #     arr[i] = arr[i - 1] + arr[i - 2]

        # return arr[n]
        first = 1
        second = 2
        if first == n:
            return n
        for i in range(3, n + 1):
            temp = second
            second = first + second
            first = temp
        return second
