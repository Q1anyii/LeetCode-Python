"""
题目：31. 下一个排列 (nextPermutation)
难度：中等
分类：数组/矩阵
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
整数数组的一个排列就是将其所有成员以序列或线性顺序排列。
下一个排列是指其按字典序排列的下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    nums1 = [1, 2, 3]
    sol.nextPermutation(nums1)
    assert nums1 == [1, 3, 2]
    nums2 = [3, 2, 1]
    sol.nextPermutation(nums2)
    assert nums2 == [1, 2, 3]
    nums3 = [1, 1, 5]
    sol.nextPermutation(nums3)
    assert nums3 == [1, 5, 1]
    nums4 = [1]
    sol.nextPermutation(nums4)
    assert nums4 == [1]
    nums5 = [1, 3, 2]
    sol.nextPermutation(nums5)
    assert nums5 == [2, 1, 3]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
