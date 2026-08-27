"""
题目：64. 最小路径和 (minPathSum)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个包含非负整数的 m x n 网格 grid，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert sol.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    assert sol.minPathSum([[1]]) == 1
    assert sol.minPathSum([[1, 2], [1, 1]]) == 3
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
