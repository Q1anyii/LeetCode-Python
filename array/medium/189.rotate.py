"""
题目：189. 轮转数组 (rotate)
难度：中等
分类：数组/矩阵
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1：
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        pass
        def reverse(left, right):
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums1, 3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]
    nums2 = [-1, -100, 3, 99]
    sol.rotate(nums2, 2)
    assert nums2 == [3, 99, -1, -100]
    nums3 = [1, 2]
    sol.rotate(nums3, 3)
    assert nums3 == [2, 1]
    nums4 = [1]
    sol.rotate(nums4, 0)
    assert nums4 == [1]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
