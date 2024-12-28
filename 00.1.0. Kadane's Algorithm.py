def bruteForce(nums):
    maxSum = nums[0]

    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum


def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [4, -1, 2, -7, 3, 4]

print(kadanes(list1))
print(kadanes(list2))


def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return [maxL, maxR]


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [4, -1, 2, -7, 3, 4]
list3 = [-1, -1, -1, -1, -1, -1]
list4 = [-10, -1, -2, -5]
print(slidingWindow(list1))
print(slidingWindow(list2))
print(slidingWindow(list3))
print(slidingWindow(list4))


# 我自己的思路
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    L, R = 0, 0
    maxL, maxR = 0, 0  # 这是很重要的，防止最后什么都不返回

    for R in range(len(nums)):
        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R
        if curSum < 0:
            curSum = 0
            L = R + 1

    return [maxL, maxR]


def kadanes(nums):
    maxSum = float("-inf")
    curSum = 0

    for n in nums:
        curSum = max(n, curSum + n)  # 更新当前子数组和
        if maxSum < curSum:
            maxSum = curSum  # 更新全局最大子数组和

    return maxSum
