from typing import Optional, List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        nums.sort()

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return

            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            # 如果当前元素 nums[i] 与下一个元素 nums[i + 1] 相同，
            # 就不断地跳过这些重复的元素，避免生成重复的子集
            # 递归调用，继续处理下一个与当前元素不同的位置 i + 1
            dfs(i + 1)

        dfs(0)
        return ans
