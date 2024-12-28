# 技巧性很强，将本题目列表中独特的性质看成无指针的链表
# 解决方案：使用快慢指针（Floyd's Tortoise and Hare 算法），将数组看成是一个无指针的链表。


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


# 问题分析
# 数组的性质：题目给定的数组长度为 n + 1，其中数字的范围是 1 到 n，并且只有一个重复的数字。这些性质意味着我们在数组中一定能找到一个重复的数字。
# 重复数字的特性：由于数字范围是 1 到 n，但数组长度是 n + 1，所以至少有两个位置存储了相同的数字。也就是说，数组存在一个循环。
# 环的检测
# 链表环的检测：在链表中检测环时，我们可以使用快慢指针（Floyd's Tortoise and Hare）算法。这个算法有两个指针，一个快指针每次走两步，一个慢指针每次走一步。如果链表中有环，快指针和慢指针最终会相遇。
# 应用到数组
# 将数组视为链表：可以将数组中的值视为指向下一个位置的指针。例如，如果数组中某个位置 i 存储的值是 j，我们可以认为这是一个从位置 i 指向位置 j 的指针。
# 构建环形链表：由于数组中有重复的数字，这意味着数组中的某些位置会指向同一个位置，形成一个环。这与链表中的环非常类似。
