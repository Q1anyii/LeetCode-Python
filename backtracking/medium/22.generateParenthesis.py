"""
题目：22. 括号生成 (generateParenthesis)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass
        def backtrack(path, left, right):
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sol.generateParenthesis(1) == ["()"]
    assert sol.generateParenthesis(2) == ["(())", "()()"]
    assert len(sol.generateParenthesis(4)) == 14
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
