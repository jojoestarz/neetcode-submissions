class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #access value using array
        #prepare res and solution path to hold possibilities
        res = []
        solution = []
        
        def dfs(index): #select the current number
            if index == len(nums):
                res.append(solution[:])
                return
            
            solution.append(nums[index]) #decision 1
            dfs(index + 1)

            solution.pop()
            dfs(index + 1) #continue to next value for more possibilities


        dfs(0)
        return res