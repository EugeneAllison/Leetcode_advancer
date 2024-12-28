def longestSubarray(nums):
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[R] != nums[L]:
            L = R
        length = max(length, R - L + 1)

    return length

# find length of minimum size subarray where the sum is greater than or equal to the target: O(n)


def shortestSubarray(nums, target):
    L = 0
    length = float('inf')
    total = 0

    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(length, R - L + 1)
            L += 1
            total -= nums[L]
    
    return length if length != float('inf') else 0

arr = [2, 3, 1, 2, 4, 3]
print(shortestSubarray(arr, 6))
