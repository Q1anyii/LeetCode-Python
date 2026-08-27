"""
题目：3. 无重复字符的最长子串 (lengthOfLongestSubstring)
难度：中等
分类：滑动窗口
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。

示例 1：
输入: s = "abcabcbb"
输出: 3

示例 2：
输入: s = "bbbbb"
输出: 1

示例 3：
输入: s = "pwwkew"
输出: 3
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring("au") == 2
    assert sol.lengthOfLongestSubstring("abba") == 2
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
