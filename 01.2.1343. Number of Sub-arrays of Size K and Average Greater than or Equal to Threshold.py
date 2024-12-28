from typing import Optional, List


# threshold 门槛
# 总结：一定要动笔画图，为什么现在没有画图和写字分析的习惯了？必须写字或画图帮助理解
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        curSum = sum(arr[: k - 1])
        # 注意：不包括元素k - 1

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if curSum / k >= threshold:
                count += 1
            curSum -= arr[L]

        return count


# 自己想的，当数不明白个数的时候，一定要画图帮助理解，一定不会错
class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        count = 0
        L = 0
        curSum = sum(arr[0 : k - 1])
        # 注意：不包括元素k - 1

        for R in range(k - 1, len(arr)):
            curSum += arr[R]
            if curSum / k >= threshold:
                count += 1
            curSum -= arr[L]
            L += 1

        return count
