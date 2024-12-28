# 画图解决问题，画图并用数学的方式解决
# 我自己的方法，使用了空间换时间：
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prefixArr(nums):
            curMultiplication = 1
            arr = []

            for num in nums:
                curMultiplication *= num
                arr.append(curMultiplication)
            return arr

        def suffixArr(nums):
            curMultiplication = 1
            arr = []
            for num in reversed(nums):
                curMultiplication *= num
                arr.append(curMultiplication)
            return list(reversed(arr))

        prefixArr = prefixArr(nums)
        suffixArr = suffixArr(nums)
        res = []

        for i in range(len(nums)):
            prev = prefixArr[i - 1] if i > 0 else 1
            next = suffixArr[i + 1] if i < len(nums) - 1 else 1
            res.append(prev * next)

        return res


# 视频方法：
# 空间不再分配给多余的两个数组
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)  # 初始化结果数组，所有元素都为1
        prefix = 1  # 前缀积初始化为1

        # 计算前缀积，并存储在结果数组中
        for i in range(len(nums)):
            res[i] *= prefix  # 将当前前缀积存入结果数组的当前位置
            prefix *= nums[i]  # 更新前缀积

        postfix = 1  # 后缀积初始化为1

        # 计算后缀积，并更新结果数组
        for i in range(len(nums) - 1, -1, -1):
            # len(nums) - 1: 数组的最后一个元素的索引。例如，如果 nums 的长度为 5，那么最后一个元素的索引就是 4（即 5 - 1）。
            # -1: 表示循环到索引 0 为止，但不包括 -1。
            # -1: 每次迭代时，索引值减少 1。
            res[i] *= postfix  # 将当前后缀积乘入结果数组的当前位置
            postfix *= nums[i]  # 更新后缀积

        return res  # 返回结果数组
