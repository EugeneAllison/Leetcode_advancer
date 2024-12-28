from typing import Optional, List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 1
        res, prev = 1, ""

        while R < len(arr):
            if arr[R] > arr[R - 1] and prev != "down":
                res = max(res, R - L + 1)
                prev = "down"
                R += 1
            elif arr[R] < arr[R - 1] and prev != "up":
                res = max(res, R - L + 1)
                prev = "up"
                R += 1
            else:
                R = R + 1 if arr[R] == arr[R - 1] else R
                L = R - 1
                prev = ""

        return res
