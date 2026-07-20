class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            leftover = target - nums[i]

            if leftover in seen:
                return [seen[leftover],i]
            seen[nums[i]] = i