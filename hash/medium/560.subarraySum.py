"""
题目：560. 和为 K 的子数组 (subarraySum)
难度：中等
分类：哈希表
"""
from collections import defaultdict
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
子数组：表示连续的序列，那么就可以对nums做循环
暴力解法：
    对nums做两次循环，
    sum = nums[i]
     if sum == k?
        ans +=1
    else:
        sum += nums[j]
        if sum == k?
            ans +=1 
            
m2:核心：不枚举所有子数组，利用前缀和公式，用哈希表记录前缀和出现次数，时间复杂度 O (n)。
    累加pre_sum, 当pre_sum - k 作为key存储在map中，

"""

# ==================== 代码实现 ====================
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ans = 0
        # for i in range(len(nums)):
        #     sum = nums[i]
        #     if sum == k:
        #         ans += 1
        #     else:
        #         for j in range(i + 1, len(nums)):
        #             sum += nums[j]
        #             if sum == k:
        #                 ans += 1

        count = 0 #用于记录子数组出现次数
        pre_sum = 0 #初始化前缀和
        mp = defaultdict(int)
        mp[0] = 1  # 前缀和0出现1次

        for num in nums:
            pre_sum += num
            # 找 pre_sum - k 是否存在
            if (pre_sum - k) in mp:
                count += mp[pre_sum - k]
            mp[pre_sum] += 1
        return count



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
