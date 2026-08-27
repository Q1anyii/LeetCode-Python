"""
题目：32. 最长有效括号 (longestValidParentheses)
难度：困难
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.longestValidParentheses("(()") == 2
    assert sol.longestValidParentheses(")()())") == 4
    assert sol.longestValidParentheses("") == 0
    assert sol.longestValidParentheses("()(()") == 2
    assert sol.longestValidParentheses("()(())") == 6
    assert sol.longestValidParentheses("((()))") == 6
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
