from typing import Optional, List
from collections import deque, Counter
from bisect import bisect_left, bisect_right
from functools import cache


# immutable 永恒的;不可改变的
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0

        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        prefixRight = self.prefix[right]
        prefixLeft = self.prefix[left - 1] if left > 0 else 0
        return prefixRight - prefixLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
