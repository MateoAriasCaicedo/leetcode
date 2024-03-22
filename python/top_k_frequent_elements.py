from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # number : count
        frequency = [[] for _ in range(len(nums) + 1)]

        for number in nums:
            count[number] = 1 + count.get(number, 0)

        for number, count in count.items():
            frequency[count].append(number)

        output = []

        for i in range(len(frequency) - 1, 0, -1):
            for number in frequency[i]:
                output.append(number)
                if len(output) == k:
                    return output
