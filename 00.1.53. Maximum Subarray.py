from typing import Optional, List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        L, R = 0, 0

        for R in range(len(nums)):
            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0

        return maxSum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


