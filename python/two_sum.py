from typing import List


# Problem link: https://leetcode.com/problems/two-sum/
# Complexity: Time of O(n) and memory O(n).
def two_sum(numbers: List[int], target: int) -> List[int]:
    previous_numbers = {}  # number : index

    for index, number in enumerate(numbers):
        difference = target - number

        if difference in previous_numbers:
            return [previous_numbers[difference], index]

        previous_numbers[number] = index

    # As we are ensured that there is a solution, we expect that the code does not reach here.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return two_sum(nums, target)
