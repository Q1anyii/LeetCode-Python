"""
题目：560. 和为 K 的子数组 (subarraySum)
难度：中等
分类：哈希表
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums 和一个整数 k，请你统计并返回该数组中和为 k 的子数组的个数。
子数组是数组中元素的连续非空序列。

示例 1：
输入：nums = [1,1,1], k = 2
输出：2

示例 2：
输入：nums = [1,2,3], k = 3
输出：2
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 3], 3) == 2
    assert sol.subarraySum([1, -1, 0], 0) == 3
    assert sol.subarraySum([-1, -1, 1], 0) == 1
    assert sol.subarraySum([1], 1) == 1
    assert sol.subarraySum([1], 0) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
