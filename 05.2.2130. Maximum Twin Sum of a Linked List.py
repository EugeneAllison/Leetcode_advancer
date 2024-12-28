# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方法一转换列表，需要空间复杂度O(n)，我自己的想法
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        values = []

        while cur:
            values.append(cur.val)
            cur = cur.next

        maxSum = 0
        curSum = 0
        l, r = 0, len(values) - 1
        while l < r:
            curSum = values[l] + values[r]
            maxSum = max(maxSum, curSum)
            l += 1
            r -= 1
        
        return maxSum

# 方法二不转换列表，需要空间复杂度O(1), 找到中间反转前半部分就ok了，我自己的想法
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseLinkedList(head):
            if not head:
                return None
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        list1 = slow.next
        slow.next = None
        list2 = reverseLinkedList(head)

        maxSum = 0
        curSum = 0
        while list1 and list2:
            curSum = list1.val + list2.val
            maxSum = max(maxSum, curSum)
            list1 = list1.next
            list2 = list2.next

        return maxSum

# 方法三需要空间复杂度O(n), 找到中间前，将结果入栈，看评论区的想法，很简单，画图辅助理解
# 方法四视频方法，不用单独创建reverse函数，在迭代中完成反转链表
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return res