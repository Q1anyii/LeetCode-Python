"""
题目：295. 数据流的中位数 (MedianFinder)
难度：困难
分类：堆
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
实现 MedianFinder 类:
- MedianFinder() 初始化 MedianFinder 对象。
- void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
- double findMedian() 返回到目前为止所有元素的中位数。

示例 1：
输入：["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出：[null, null, null, 1.5, null, 2.0]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class MedianFinder:
    pass
    def __init__(self):
        pass
    def addNum(self, num: int) -> None:
        pass
    def findMedian(self) -> float:
        pass


# ==================== 测试用例 ====================
def test_solution():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    mf2 = MedianFinder()
    mf2.addNum(5)
    assert mf2.findMedian() == 5.0
    mf2.addNum(3)
    assert mf2.findMedian() == 4.0
    mf2.addNum(4)
    assert mf2.findMedian() == 4.0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
