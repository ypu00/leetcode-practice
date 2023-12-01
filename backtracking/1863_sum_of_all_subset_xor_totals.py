from typing import List

class Solution:

    def __init__(self):
        self.total_sum = 0

    def subsetXORSum(self, nums: List[int]) -> int:

        def get_xor_total(curr_set) -> int:
            xor_total = curr_set[0]

            for i in range(1, len(curr_set)):
                xor_total = xor_total ^ curr_set[i]

            return xor_total            

        def backtrack(start, curr_set):

            if start > len(nums):
                return

            if curr_set:
                if len(curr_set) == 1:
                    self.total_sum += curr_set[0]
                else:
                    self.total_sum += get_xor_total(curr_set)

            for i in range(start, len(nums)):
                curr_set.append(nums[i])
                backtrack(i + 1, curr_set)
                curr_set.pop()
    
        backtrack(0, [])

        return self.total_sum