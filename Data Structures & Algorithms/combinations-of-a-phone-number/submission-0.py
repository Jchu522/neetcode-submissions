class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # a = ord('a')
        mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        res = []
        for i in digits:
            temp = res
            res = []
            if not temp:
                for j in mapping[int(i)]:
                    res.append(j)
            for j in mapping[int(i)]:
                for pre in temp:
                    res.append(pre+j)
            # print(res)
        
        return res
        # ret = ["" for _ in range(3 ** digits)]
        # for i in digits:
        #     temp = 0
        #     for j in range(len(ret)):
        #         if j > len(ret) // 3: 



