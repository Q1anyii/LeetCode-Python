"""
题目：347. 前 K 个高频元素 (topKFrequent)
难度：中等
分类：堆
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums 和一个整数 k，请你返回其中出现频率前 k 高的元素。你可以按任意顺序返回答案。

示例 1：
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2：
输入: nums = [1], k = 1
输出: [1]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sol.topKFrequent([1], 1) == [1]
    assert sorted(sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)) == [-1, 2]
    assert sorted(sol.topKFrequent([1, 2], 2)) == [1, 2]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
