class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0

        for num in nums:
            total += num

        if(total % 2 != 0):
            return False

        state_dct = {}

        return self.find_combination(nums, 0, 0, total, state_dct)

    def find_combination(self, array, index, curr_sum, total, state_dct):
        current = str(index) + '' + str(curr_sum)

        if(current in state_dct.keys()):
            return state_dct[current]

        # Base cases
        if(curr_sum * 2 == total):
            return True

        if(curr_sum > total or index >= len(array)):
            return False

        partition_found = self.find_combination(array, index+1, curr_sum, total, state_dct) or self.find_combination(
            array, index + 1, curr_sum + array[index], total, state_dct)
        state_dct[current] = partition_found

        # Other cases
        return partition_found
