"""
题目：287. 寻找重复数 (findDuplicate)
难度：中等
分类：双指针
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 [1, n] 范围内，可知至少存在一个重复的整数。
假设 nums 只有一个重复的整数，返回这个重复的数。
你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert sol.findDuplicate([1, 1]) == 1
    assert sol.findDuplicate([1, 1, 2]) == 1
    assert sol.findDuplicate([2, 2, 2, 2, 2]) == 2
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
