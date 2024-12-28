# prefix: 前缀, postfix/suffix: 后缀, query: 疑问，质询
# prefix array: must be the contiguous(连续的) subarray from the array index 0
# 使用prefix sum 来提前储存是非常有用的技巧


class PrefixSum:
    def __init__(self, nums):
        self.prefix = []

        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def query(self, left, right):
        preRight = self.prefix[right]
        # 如果你在 __init__ 方法中只使用局部变量 prefix，如下面的代码所示：preRight = prefix[right]  这里会报错，因为 prefix 在此作用域不可见。当你尝试在 query 方法中访问 prefix 时，会报错，因为 prefix 是 __init__ 方法的局部变量，在 query 方法中不可见。
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return preRight - preLeft


# 实例变量 vs 局部变量
# 实例变量 (self.prefix)：
# 实例变量是绑定到类实例（对象）的变量。每个实例都有自己独立的实例变量。
# 使用 self.prefix，可以确保变量在类的其他方法中也是可访问的。
# 例如：self.prefix = [] 创建了一个绑定到实例的列表，该列表在整个实例的生命周期中可用。

# 局部变量 (prefix)：
# 局部变量只在方法内有效。当方法执行完毕后，局部变量会被销毁。
# 如果使用 prefix = []，该变量在 __init__ 方法外部不可见，因此不能在类的其他方法中使用。
