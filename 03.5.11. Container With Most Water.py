# 双指针问题好像总是从for循环嵌套暴力解法中找到有规律，不可回头的一部分，将O(n^2)直接优化变成O(n)
# 双指针就是两种方式：双侧向内夹，单侧亦步亦趋
# 我想到的暴力解法：
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)

        return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = (right - left) * min(height[right], height[left])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, (right - left) * min(height[right], height[left]))
        
        return max_area

