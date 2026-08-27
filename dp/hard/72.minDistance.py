"""
题目：72. 编辑距离 (minDistance)
难度：困难
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你两个单词 word1 和 word2，请返回将 word1 转换成 word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：
1. 插入一个字符
2. 删除一个字符
3. 替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.minDistance("horse", "ros") == 3
    assert sol.minDistance("intention", "execution") == 5
    assert sol.minDistance("", "a") == 1
    assert sol.minDistance("a", "") == 1
    assert sol.minDistance("abc", "abc") == 0
    assert sol.minDistance("sea", "eat") == 2
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
