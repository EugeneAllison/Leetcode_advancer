# find the middle of the linked list
# time O(n), space O(1)


def middle_of_list(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# determine if a linked list has a cycle
# 可以用hash set，不过空间复杂度是O(n)
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# determine if a linked list has a cycle, and return the head of the cycle otherwise return Null
def cycle_start(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # 总会跳出循环，查看是因为 1.相遇break出循环 还是 2.没环fast到头出循环：判断fast状态
    if not fast or not fast.next:
        return None

    slow_2 = head
    while slow != slow_2:
        slow = slow.next
        slow_2 = slow_2.next

    return slow


# 数学上的解释如下：

# 设环的起点为 C，从头到环起点的距离为 a。
# 设 slow 和 fast 在环中相遇时，从 C 到相遇点的距离为 b。
# 环的总长度为 L。
# 可以得到以下等式：

# slow 走了 a + b 步。
# fast 走了 2(a + b) 步（因为 fast 速度是 slow 的两倍）。
# 因为 fast 比 slow 多走了一圈，所以有 2(a + b) = a + b + nL（n 为环中走的圈数）。
# 化简得：a + b = nL，即 a = nL - b。

# 这意味着，从相遇点到环起点的距离 a 等于从链表头到环起点的距离。因此，当我们同时移动 slow 和 slow_2 时，它们会在环起点相遇。
