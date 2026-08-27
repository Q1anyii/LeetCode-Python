"""
题目：56. 合并区间 (merge)
难度：中等
分类：数组/矩阵
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert sol.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert sol.merge([]) == []
    assert sol.merge([[1, 2]]) == [[1, 2]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
