class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {}

        for index, value in enumerate(nums):
            checkValue = target - value
            if checkValue in stored:
                return [stored[checkValue], index]
            stored[value] = index
        return []