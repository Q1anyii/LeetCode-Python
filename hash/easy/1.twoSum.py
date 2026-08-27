"""
题目：1. 两数之和 (twoSum)
难度：简单
分类：哈希表
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
"""


# ==================== 解题思路 ====================
"""
需要返回下表，又需要结合元素进行判断，如果需要最快速获取元素，使用hashtable是最优解
hashtable按照{num: idx} 存储，因为最后需要返回下标
因此需要初始化一个hashtable，判断hashtable中的元素是否包含target-（num in nums）
如果包含，则返回下标，否则存入元素
当遍历完仍然不存在，说明不符合返回空
"""

# ==================== 代码实现 ====================
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashtable:
                return [hashtable.get(diff), i]
            hashtable[num] = i
        return []


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]
    assert sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
