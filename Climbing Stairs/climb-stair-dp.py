class Solution:
    def climbStairs(self, n: int) -> int:
        count_dct = {}
        count_dct[0] = 1
        count_dct[1] = 1

        for i in range(2, n + 1):
            count_dct[i] = count_dct[i-1] + count_dct[i-2]

        return count_dct[n]
