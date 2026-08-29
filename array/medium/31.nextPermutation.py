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
倒序遍历，判断nums[i] >= nums[i + 1]
        true: 表示当前序列是降序,无更大序列，需要改变i位置, i - 1
        false: 当前序列是升序，没必要再判断
        当序列是升序，取大于i的最小数，用于交换位置
        如果始终是降序，则需倒排
        取left和right，进行指针交换
        
"""

# ==================== 代码实现 ====================
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
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
