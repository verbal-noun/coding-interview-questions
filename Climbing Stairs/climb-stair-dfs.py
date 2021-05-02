class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        return self.find_combinations(0, n, count)

    def find_combinations(self, curr, target):

        # Base cases
        if(curr == target):
            # count += 1
            return 1

        if(curr > target):
            return 0

        return self.find_combinations(curr + 1, target, count) + self.find_combinations(curr + 2, target, count)
