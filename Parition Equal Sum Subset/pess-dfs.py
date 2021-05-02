# This solutin is theoretically correct but gives Time limit exceeded
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0

        for num in nums:
            total += num

        if(total % 2 != 0):
            return False

        return self.find_combination(nums, 0, 0, total)

    def find_combination(self, array, index, curr_sum, total):
        # Base cases
        if(curr_sum * 2 == total):
            return True

        if(curr_sum > total or index >= len(array)):
            return False

        # Other cases
        return self.find_combination(array, index+1, curr_sum, total) or self.find_combination(array, index + 1, curr_sum + array[index], total)
