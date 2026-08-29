"""
题目：53. 最大子数组和 (maxSubArray)
难度：中等
分类：数组/矩阵
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


# ==================== 解题思路 ====================
"""
维护当前最大值和全局最大值，默认为第一个元素
对nums遍历
判断当前最大值=max(curr_max, curr_max + num)
全局最大值 = max(global_max, curr_max)
"""

# ==================== 代码实现 ====================
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = global_max = nums[0]
        for num in nums[1:]:
            cur_max = max(num, cur_max + num)
            global_max = max(global_max, cur_max)
        return global_max


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArray([-1]) == -1
    assert sol.maxSubArray([-2, -1]) == -1
    assert sol.maxSubArray([-1,0,-2]) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
