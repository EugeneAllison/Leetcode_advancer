from typing import Optional, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitToChar[digits[i]]:
                dfs(i + 1, curStr + c)
                # 由于字符串是不可变的，传递给递归函数的 curStr + c 是一个全新的对象，而不会影响当前递归层次中的 curStr。
                # 因为每次递归都生成新的字符串并传递下去，当前递归层的 curStr 不会因为递归调用而变化，所以不需要像列表那样使用 pop 操作来回溯恢复现场。

        if digits:
            dfs(0, "")
        # 这部分代码是用来检查 digits 是否为空字符串。（该题目输出标准标准形式的要求）
        # 如果 digits 为空字符串，即用户输入的数字序列是空的，那么就没有任何字母组合需要生成，程序不会执行后续的 DFS 调用。
        # 如果 digits 不为空，表示用户输入了有效的数字序列，则继续执行后面的代码。

        return res
