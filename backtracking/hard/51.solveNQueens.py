"""
题目：51. N 皇后 (solveNQueens)
难度：困难
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n，返回所有不同的 n 皇后问题的解决方案。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass
        def backtrack(row):
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    result = sol.solveNQueens(4)
    assert len(result) == 2
    assert ".Q.." in result[0]
    assert sol.solveNQueens(1) == [["Q"]]
    assert len(sol.solveNQueens(8)) == 92
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
