from typing import Optional, List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int) -> None:
            d = k - len(path)  # 还要选 d 个数
            if d == 0:  # 选好了
                ans.append(path.copy())
                return
            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()  # 恢复现场

        dfs(n)
        return ans


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int) -> None:
            d = k - len(path)  # 还要选 d 个数
            if d == 0:  # 选好了
                ans.append(path.copy())
                return
            # 如果 i > d，可以不选 i
            # 即当前数字比剩余需要选择的数字多，那么可以不选 i，直接递归到 i-1 继续判断。
            # 因为 d 表示还需要选择的元素个数，而 i 是当前可选的数字，如果 i 大于 d，意味着即使选择了 i，后续也会缺少足够的数字来凑齐 d 个数。
            if i > d:
                dfs(i - 1)
            # 选 i
            path.append(i)
            dfs(i - 1)
            path.pop()  # 恢复现场

        dfs(n)
        return ans
