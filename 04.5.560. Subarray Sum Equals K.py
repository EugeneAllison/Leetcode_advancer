from typing import Optional, List
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from functools import cache
from itertools import pairwise
import heapq


# 我的思路，错误代码：
# 你的代码试图通过滑动窗口方法来找到数组中和为 k 的子数组数量。然而，滑动窗口方法适用于非负数数组，因为滑动窗口主要用于处理范围内递增的情况。对于这个问题（和为 k 的子数组数量），我们需要使用前缀和及哈希表来解决问题。这是因为数组中可能包含负数，使得滑动窗口方法无法正确处理。

# 下面是你的代码中的问题及其解释：
# 滑动窗口方法的限制：滑动窗口方法通常用于处理所有元素为非负数的情况，但在数组中可能存在负数的情况下，这种方法无法正确处理。
# 逻辑错误：在处理 totalSum 大于 k 的情况下，你不断地从左侧减少 totalSum，但是这并不能保证找到所有和为 k 的子数组。

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        totalSum = 0
        count = 0

        for r in range(len(nums)):
            totalSum += nums[r]
            while l < r:
                if totalSum < k:
                    break
                elif totalSum > k:
                    totalSum -= nums[l]
                    l += 1
                else:
                    count += 1
                    totalSum -= nums[l]
                    l += 1

        return count

# 先写一个暴力算法，可以发现在这个过程中可以加入prefixSum进行优化（画图）
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalSum = 0
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                totalSum = sum(nums[i:j+1])
                if totalSum == k:
                    count += 1

        return count


# 很巧妙的思路，不好理解可以看视频
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0  # 初始化结果计数器
        curSum = 0  # 初始化当前前缀和
        prefixSum = {0: 1}  # 初始化前缀和哈希表，{前缀和: 出现次数}

        for n in nums:
            curSum += n  # 更新当前前缀和
            diff = curSum - k  # 计算当前前缀和与 k 的差值
            res += prefixSum.get(diff, 0)  # 如果差值在哈希表中，累加其出现次数到结果中
            prefixSum[curSum] = (
                prefixSum.get(curSum, 0) + 1
            )  # 更新哈希表中当前前缀和的出现次数

        return res  # 返回满足条件的子数组数量
