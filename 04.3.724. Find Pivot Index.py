# 我自己的思路，空间换时间：
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        def prefixSumArr(nums):
            prefixSum = [0]
            curSum = 0

            for num in nums:
                curSum += num
                prefixSum.append(curSum)
            prefixSum.pop()
            return prefixSum

        def postfixSumArr(nums):
            postfixSum = [0]
            curSum = 0

            for num in reversed(nums):
                curSum += num
                postfixSum.append(curSum)
            postfixSum.pop()
            return list(reversed(postfixSum))   # 将迭代器转换回列表
        # 为什么要写 list(reversed(postfixSum)) 而不是直接写 reversed(postfixSum)
        # reversed(postfixSum) 返回的是一个 list_reverse_iterator 对象，这实际上是一个迭代器。list(reversed(postfixSum)) 将这个迭代器转换回列表。
        # 迭代器不支持索引操作（例如 postfixSumArr[i]），你不能直接通过索引访问其中的元素。列表支持索引操作，可以直接访问特定位置的元素。

        prefixSumArr = prefixSumArr(nums)
        postfixSumArr = postfixSumArr(nums)

        for i in range(len(nums)):
            if prefixSumArr[i] == postfixSumArr[i]:
                return i

        return -1

# 我自己的思路，暴力写法，效率非常低：
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i+1:])
            if leftSum == rightSum:
                return i
        return -1

# 视频解法：
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
            # or just say: left_sum += nums[i]
        return -1