class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for char in s:
            if char.isalnum():
                newStr += char.lower()

        return newStr == newStr[::-1]

class Solution:
    def alphaNumber(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNumber(s[l]):
                # 为什么不能去除 l < r
                # 假设字符串为 ".,.", 而 l 初始为 0，r 初始为 3。如果直接执行 while not self.alphaNumber(s[l]):，l 会一直增加，超出 r，导致越界错误。同理，r 也会超出 l。
                l += 1
            while l < r and not self.alphaNumber(s[r]):
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
