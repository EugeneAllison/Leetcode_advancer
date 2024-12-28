from typing import Optional, List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return

            dfs(i + 1)

            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return ans


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            ans.append(path.copy())

            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return ans
