# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                # 注意不是.val，要比较的不是数值
                return True

        return False     

# 用hash set，不过空间复杂度是O(n):
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        hashSet = set()
        while cur:
            if cur not in hashSet:
                hashSet.add(cur)
            else:
                return True
            cur = cur.next
        
        return False
