from functools import reduce 

class Solution: 
    def threeSum(self, A): 

        # Sort the input array 
        A.sort()

        # Track the unique sets and seen 
        seen = set()
        all_three_sums = []
        second_last_index = len(A) - 2

        for i in range(0, second_last_index):
            self.find_two_sum(i, A, all_three_sums, seen)

        return all_three_sums


    def find_two_sum(self, root_index, A, all_three_sums, seen): 
        # Establish left and right pointer 
        left = root_index + 1
        right = len(A) - 1 

        # Search through the array until we have exhausted
        while left < right: 
            three_number_sum = A[root_index] + A[left] + A[right]

            if(three_number_sum == 0):
                number_list = [A[root_index], A[left], A[right]]
                number_list.sort()

                # Creating a string signature, ie '-121' to use in set 
                signature = reduce(lambda acc, num: str(acc) + 
                    str(num), number_list)
                
                if signature not in seen: 
                    all_three_sums.append(number_list)
                    seen.add(signature)

            # Moving the pointers 
                left += 1
                right -= 1
            elif three_number_sum < 0:
                left += 1
            else:
                right -= 1