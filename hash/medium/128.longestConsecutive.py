"""
题目：128. 最长连续序列 (longestConsecutive)
难度：中等
分类：哈希表
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个未排序的整数数组 nums，找出数字连续的最长序列的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""


# ==================== 解题思路 ====================
"""
O(n^2)设置一个dict，将各个元素设置为key，value为它之后连续的序列长度
第1个元素，判断数组中是否存在比该元素+1的数字，如果有，value+1，

method2:
将nums转为set去重，初始化max_len作为最长序列长度
for num in nums
如果num-1存在，说明当前num并非连续序列中的最小值，所以没必要从它开始遍历
如果不存在，说明当前num为连续序列最小值，
    因此开始从num遍历，
    初始化curr = num， len = 1
    每遍历一次就更新curr，同时动态更新len，
    最后maxlen = max（len， maxlen）
    return maxlen

"""

# ==================== 代码实现 ====================
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            # 关键优化：只从起点开始数
            if num - 1 not in num_set:
                current_num = num
                current_len = 1

                # while 循环累加，但整个数组累计只跑 O(n) 次
                while current_num + 1 in num_set:
                    current_num += 1
                    current_len += 1

                max_len = max(max_len, current_len)

        return max_len  # 空数组时返回 0，不需要 default


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutive([1]) == 1
    assert sol.longestConsecutive([1, 2, 0, 1]) == 3
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
