# 技巧性很强的一题
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        minMax = []
        rain = []
        maxTemp = 0

        for h in height:
            maxTemp = max(h, maxTemp)
            maxLeft.append(maxTemp)

        maxTemp = 0
        for h in height[::-1]:
            maxTemp = max(h, maxTemp)
            maxRight.append(maxTemp)

        maxRight = maxRight[::-1]

        for i in range(len(height)):
            minMax.append(min(maxLeft[i], maxRight[i]))

        for i in range(len(height)):
            if minMax[i] - height[i] >= 0:
                rain.append(minMax[i] - height[i])

        return sum(rain)
