"""
题目：34. 在排序数组中查找元素的第一个和最后一个位置 (searchRange)
难度：中等
分类：二分查找
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
"""


# ==================== 解题思路 ====================
"""
二分查找，使用mid找到target所在idx
先找左边：如果找到了target，先标记，再向左查找，如果还有target，就更新
右边于左边相似，但第二步向右查找
"""

# ==================== 代码实现 ====================
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left():
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    right = mid - 1  # 继续往左边找，看有没有更早出现的target
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        def find_right():
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    left = mid + 1  # 继续往左边找，看有没有更早出现的target
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        return [find_left(), find_right()]


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert sol.searchRange([], 0) == [-1, -1]
    assert sol.searchRange([1], 1) == [0, 0]
    assert sol.searchRange([2, 2], 2) == [0, 1]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
