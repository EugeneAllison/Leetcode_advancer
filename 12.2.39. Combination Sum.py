from typing import Optional, List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, path, total):
            if total == target:
                ans.append(path[:])
                return

            if (
                i >= len(candidates) or total > target
            ):  # 剪枝：没有多余元素了，或者现在的数已经超过要求了
                # 剪枝核心：要么太小（少），要么太大（多）
                return

            path.append(candidates[i])
            dfs(i, path, total + candidates[i])  # 可以反复的选择同一个数字
            path.pop()

            dfs(i + 1, path, total)

        dfs(0, [], 0)
        return ans


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, sum):
            if sum == target:
                ans.append(path.copy())
                return

            if i == len(candidates) or sum > target:
                return

            path.append(candidates[i])
            dfs(i, sum + candidates[i])
            path.pop()

            dfs(i + 1, sum)

        dfs(0, 0)
        return ans


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, sum):
            if sum == target:
                ans.append(path.copy())
                return
            if i == len(candidates) or sum > target:
                return

            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j, sum + candidates[j])  # 同一数字可以被多次选取
                path.pop()

        dfs(0, 0)
        return ans


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i, sum):
            if sum == target:
                ans.append(path.copy())
                return
            if i == len(candidates) or sum > target:
                return

            path.append(candidates[i])
            dfs(i + 1, sum + candidates[i])
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                # 要是不选，任何相等的数字都不可再选
                i += 1
            dfs(i + 1, sum)

        dfs(0, 0)
        return ans
