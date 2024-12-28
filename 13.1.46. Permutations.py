from typing import Optional, List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, s):
            if i == len(nums):
                ans.append(path[:])
                return
            
            for x in s:
                path.append(x)
                dfs(i + 1, s - {x})
                path.pop()
        
        dfs(0, set(nums))
        return ans
    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res
    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            
            perms = new_perms
        
        return perms