"""
题目：84. 柱状图中最大的矩形 (largestRectangleArea)
难度：困难
分类：栈
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1：
输入：heights = [2,1,5,6,2,3]
输出：10

示例 2：
输入：heights = [2,4]
输出：4
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    assert sol.largestRectangleArea([1, 1]) == 2
    assert sol.largestRectangleArea([0]) == 0
    assert sol.largestRectangleArea([5]) == 5
    assert sol.largestRectangleArea([1, 2, 3, 4, 5]) == 9
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
