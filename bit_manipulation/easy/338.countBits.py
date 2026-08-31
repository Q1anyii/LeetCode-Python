"""
题目：338. 比特位计数 (countBits)
难度：简单
分类：位运算
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数 n，对于每个 i（0 <= i <= n），计算其二进制表示中 1 的个数，返回一个长度为 n + 1 的数组 ans 作为答案。

示例 1：
输入：n = 2
输出：[0,1,1]
解释：
0 --> 0 (0 个 1)
1 --> 1 (1 个 1)
2 --> 10 (1 个 1)

示例 2：
输入：n = 5
输出：[0,1,1,2,1,2]
"""


# ==================== 解题思路 ====================
"""
对n遍历，每个数都对2取余，直到余数为0
十进制转二进制：
    对二取余数，n%2, 如果n%2 == 1,标记1位，否则为0，然后n继续%2
"""

# ==================== 代码实现 ====================
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1,n+1):
            count = 0
            while i != 0:
                n = i % 2
                if n == 1:
                    count += 1
                i = int(i / 2)
            ans.append(count)
        return ans


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.countBits(2) == [0, 1, 1]
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert sol.countBits(0) == [0]
    assert sol.countBits(1) == [0, 1]
    assert sol.countBits(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
