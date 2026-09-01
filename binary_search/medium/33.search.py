"""
题目：33. 搜索旋转排序数组 (search)
难度：中等
分类：二分查找
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
整数数组 nums 按升序排列，数组中的值互不相同。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]。
给你旋转后的数组 nums 和一个整数 target，如果 nums 中存在这个目标值 target，则返回它的下标，否则返回 -1。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
"""


# ==================== 解题思路 ====================
"""
定义左右指针， 并使用二分查找
    while左指针小于右指针：
        mid = left + right // 2
        首先判断mid所在元素是否等于target，是则直接返回mid
        判断left所在位置0是否小于mid，是则表明mid左侧子数组升序
            判断left <= target < mid : 如果是，则使right = mid - 1，缩小差距
            否则说明target不在left-mid范围中，因此使left = mid + 1， 缩小差距
        否则表明左侧数组是被旋转后另一半
            判断target是否in （mid， right），是则left = mid + 1
            否则right = mid - 1
    当左指针大于右指针时，说明target不存在于数组中，返回-1
"""

# ==================== 代码实现 ====================
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid =  (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    assert sol.search([1], 1) == 0
    assert sol.search([5, 1, 3], 3) == 2
    assert sol.search([5, 1, 3], 5) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
