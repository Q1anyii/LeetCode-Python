"""
题目：79. 单词搜索 (exist)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word。如果 word 存在于网格中，返回 true；否则，返回 false。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中"相邻"单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass
        def dfs(i, j, index):
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert sol.exist(board, "ABCCED") is True
    assert sol.exist(board, "SEE") is True
    assert sol.exist(board, "ABCB") is False
    assert sol.exist([["a"]], "a") is True
    assert sol.exist([["a"]], "b") is False
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
