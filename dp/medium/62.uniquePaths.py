"""
题目：62. 不同路径 (uniquePaths)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
一个机器人位于一个 m x n 网格的左上角。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(1, 1) == 1
    assert sol.uniquePaths(2, 2) == 2
    assert sol.uniquePaths(3, 3) == 6
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
