# sliding window focus on the window itself or the sum within the window (a range)
# two pointers focus on the pointer not the window (two point)

# check if an array is a palindrome 回文


def is_palindrome(arr):
    l, r = 0, len(arr) - 1
    while l <= r:
        if arr[l] == arr[r]:
            l += 1
            r -= 1
        else:
            return False

    return True


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 2, 3, 2, 1]
list3 = [1, 2, 3, 3, 2, 1]
list4 = []
print(is_palindrome(list1))
print(is_palindrome(list2))
print(is_palindrome(list3))
print(is_palindrome(list4))


# given a sorted array, return the two indices (index - indices or indexes) of two elements which sum up to the target value. Assume there is exactly one solution.

# method one(普适方法) (不管有没有排好序) is Two Sum


def targetSum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            return [l, r]


nums1 = [2, 7, 11, 15]
print(targetSum(nums1, 9))  # output: [0, 1]
