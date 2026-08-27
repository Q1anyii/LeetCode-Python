"""
题目：70. 爬楼梯 (climbStairs)
难度：简单
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。1. 1 阶 + 1 阶 2. 2 阶

示例 2：
输入：n = 3
输出：3
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def climbStairs(self, n: int) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs(10) == 89
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
