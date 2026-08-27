"""
题目：78. 子集 (subsets)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums，数组中的元素互不相同。返回该数组所有可能的子集（幂集）。
解集不能包含重复的子集。你可以按任意顺序返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pass
        def backtrack(start, path):
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    result = sol.subsets([1, 2, 3])
    assert sorted(result) == sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert sol.subsets([0]) == [[], [0]]
    assert len(sol.subsets([1, 2, 3, 4, 5])) == 32
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
