from typing import Optional, List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = sum(nums)

        for n in nums:
            curMax = max(curMax + n, n)
            # 在遍历数组时，计算以当前元素 n 结尾的最大子数组和。
            # 具体来说，这一行代码是在做如下判断：
            # curMax + n：表示将当前元素 n 加入之前的子数组（即继续扩展当前的子数组）。
            # n：表示从当前元素 n 开始，重新计算一个新的子数组。
            # 不是先加再判断，而是先判断再加：
            # curSum = max(curSum, 0)
            # curSum += n
            curMin = min(curMin + n, n)
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
        # 如果全局最大值为负数，说明数组中所有数都是负数
