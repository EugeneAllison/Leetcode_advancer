# 我自己想到的方法：
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            while numbers[l] + numbers[r] > target:
                r -= 1
            while numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            # 为什么要加1？题目限定的要求
        return []


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
