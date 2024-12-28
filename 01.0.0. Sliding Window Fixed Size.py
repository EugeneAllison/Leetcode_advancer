# check if array contains a pare of duplicate values
# given the window size k
# detecting the duplicate values will be easy to use hash set


def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True

    return False


def closeDuplicates(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:   # 要注意有一个加1
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        else:
            window.add(nums[R])

    return False


nums = [1, 2, 3, 1, 2, 3, 4]

print(closeDuplicatesBruteForce(nums, 3))
