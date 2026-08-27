"""
题目：39. 组合总和 (combinationSum)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个无重复元素的整数数组 candidates 和一个目标整数 target，找出 candidates 中可以使数字和为目标数 target 的所有不同组合，并以列表形式返回。你可以按任意顺序返回这些组合。
candidates 中的同一个数字可以无限制重复被选取。

示例 1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass
        def backtrack(start, path, remaining):
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert sol.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sol.combinationSum([2], 1) == []
    assert sol.combinationSum([1], 1) == [[1]]
    assert sol.combinationSum([1], 2) == [[1, 1]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
