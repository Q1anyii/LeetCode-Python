"""
题目：15. 三数之和 (threeSum)
难度：中等
分类：双指针
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums，返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = [0,1,1]
输出：[]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.threeSum([0, 1, 1]) == []
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert sol.threeSum([]) == []
    assert sol.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
