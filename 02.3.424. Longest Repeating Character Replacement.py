class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        length = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while (r - l + 1) - max(count.values()) > k:
                # AI给出的写法：max(count.values()) - count[s[l]] > k:
                count[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length


# count.get(s[r], 0) 是字典的 get 方法。它尝试获取键 s[r]（即当前字符）的值。如果键不存在，则返回默认值 0。
# max(count.values()) 返回当前滑动窗口中出现次数最多的字符的出现次数。
# (r - l + 1) - max(count.values()) 计算需要替换的字符数量（即窗口总长度减去出现次数最多的字符的数量）。
