class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numS = set(nums)
        count = 0
        for i in nums:
            if (i-1) not in numS:
                streak = 0
                while (i + streak) in numS:
                    streak += 1
                count = max(streak,count)
        return count