"""
题目：85. 最大矩形 (maximalRectangle)
难度：困难
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个仅包含 0 和 1、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert sol.maximalRectangle(matrix) == 6
    assert sol.maximalRectangle([["0"]]) == 0
    assert sol.maximalRectangle([["1"]]) == 1
    assert sol.maximalRectangle([["1","1"],["1","1"]]) == 4
    assert sol.maximalRectangle([["0","1"],["1","0"]]) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
