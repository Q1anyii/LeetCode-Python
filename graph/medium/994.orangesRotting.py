"""
题目：994. 腐烂的橘子 (orangesRotting)
难度：中等
分类：图
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；值 1 代表新鲜橘子；值 2 代表腐烂的橘子。
每分钟，腐烂的橘子周围 4 个方向上相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

示例 1：
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert sol.orangesRotting([[0, 2]]) == 0
    assert sol.orangesRotting([[1]]) == -1
    assert sol.orangesRotting([[2]]) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
