class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        res = []
        while l < r: # here is when we know every value is seen
            csum = numbers[l] + numbers[r]
            if csum > target:
                r-=1
            elif csum < target:
                l+=1
            elif csum == target:
                return [l+1,r+1]
