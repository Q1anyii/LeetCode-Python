"""
题目：74. 搜索二维矩阵 (searchMatrix)
难度：中等
分类：二分查找
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个满足下述两条属性的 m x n 整数矩阵：
每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target，如果 target 在矩阵中，返回 true；否则，返回 false。
复杂度必须：O(log(m * n))
示例 1：
输入：matrix = [ [1,3,5,7],
                [10,11,16,20],
                [23,30,34,60]], target = 3
输出：true
"""


# ==================== 解题思路 ====================
"""
复杂度O(log(m * n))
将martix视为一个一位数组拉长
取m = len(martix), n = len(martix[0]),m为martix长度，n为子数组长度
因此可以计算出二维拉长为一位的长度m*n
left = 0, right = m*n - 1
再据此做二分查询,mid = (left + right) // 2
取行号row = mid // n, mid // n 表示对子数组长度取行数中间部分
取列号col = mid % n， 表示对子数组长度取余数，因此可以取子数组的中间部分
val = martix[row][col]表整个数组的中心
只要 == target,则说明target in nums
否则判断target 是否大于val
    大于表示需要取右半部分， left = mid + 1
    小于则取左半部分，right = mid - 1 
"""

# ==================== 代码实现 ====================
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        left = 0
        right = m * n - 1
        while left<= right:
            mid = (left + right) //2
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert sol.searchMatrix(matrix, 3) is True
    assert sol.searchMatrix(matrix, 13) is False
    assert sol.searchMatrix(matrix, 1) is True
    assert sol.searchMatrix(matrix, 60) is True
    assert sol.searchMatrix(matrix, 0) is False
    assert sol.searchMatrix([], 1) is False
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
