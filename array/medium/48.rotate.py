"""
题目：48. 旋转图像 (rotate)
难度：中等
分类：数组/矩阵
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1：
输入：matrix = [ [1,2,3],
                [4,5,6],
                [7,8,9]]
输出：[[7,4,1],
      [8,5,2],
      [9,6,3]]
"""


# ==================== 解题思路 ====================
"""
先转置，后左右反转
"""

# ==================== 代码实现 ====================
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 第一步：矩阵转置
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix1)
    assert matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix2)
    assert matrix2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    matrix3 = [[1]]
    sol.rotate(matrix3)
    assert matrix3 == [[1]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
