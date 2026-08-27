"""
题目：135. 分发糖果 (candy)
难度：困难
分类：贪心
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
你需要按照以下要求，给这些孩子分发糖果：
- 每个孩子至少分配到 1 个糖果。
- 相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的最少糖果数目。

示例 1：
输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def candy(self, ratings: List[int]) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.candy([1, 0, 2]) == 5
    assert sol.candy([1, 2, 2]) == 4
    assert sol.candy([1]) == 1
    assert sol.candy([1, 2, 3, 4, 5]) == 15
    assert sol.candy([5, 4, 3, 2, 1]) == 15
    assert sol.candy([1, 3, 2, 2, 1]) == 7
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
