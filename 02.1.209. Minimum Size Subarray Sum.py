from typing import Optional, List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        totalSum = 0
        left = 0

        for right in range(len(nums)):
            totalSum += nums[right]
            while totalSum >= target:
                length = min(length, right - left + 1)
                totalSum -= nums[left]
                left += 1

        return length if length != float("inf") else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        sum = 0
        l = 0

        for r, x in enumerate(nums):
            sum += x
            while sum >= target:
                ans = min(ans, r - l + 1)
                sum -= nums[l]
                l += 1

        return ans if ans <= n else 0
