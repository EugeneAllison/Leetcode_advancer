from typing import Optional, List

# trade off 权衡
# query  提问;质问，怀疑


class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    # O(n)
    @staticmethod
    # @staticmethod 是一个装饰器decorator，用于将一个方法标记为静态方法（static method）静态方法不依赖类的实例，可以直接通过类名调用。它们通常用于那些不需要访问或修改类实例状态的功能。
    def build(nums, L, R):
        if L == R:
            return SegmentTree(nums[L], L, R)

        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    # O(log n)
    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return

        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.sum = self.left.sum + self.right.sum

    # O(log n)
    def rangeQuery(self, L, R):
        if L == self.L and R == self.R:
            return self.sum

        M = (self.L + self.R) // 2
        if L > M:
            return self.right.rangeQuery(L, R)
        elif R <= M:
            return self.left.rangeQuery(L, R)
        else:
            return self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R)
