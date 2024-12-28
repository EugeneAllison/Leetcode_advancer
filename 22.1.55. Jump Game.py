from typing import Optional, List
from collections import deque, Counter
from bisect import bisect_left, bisect_right
from functools import cache


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
            
        return goal == 0
            