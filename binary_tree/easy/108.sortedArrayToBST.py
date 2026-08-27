"""
题目：108. 将有序数组转换为二叉搜索树 (sortedArrayToBST)
难度：简单
分类：二叉树
"""

from typing import List, Optional, Dict, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ==================== 题目描述 ====================
"""
给你一个整数数组 nums，其中元素已经按升序排列，请你将其转换为一棵高度平衡二叉搜索树。
高度平衡二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1」的二叉树。

示例 1：
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        pass
        def build(left, right):
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    result = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    assert result.val == 0
    assert result.left.val == -10
    assert result.left.right.val == -3
    assert result.right.val == 5
    assert result.right.right.val == 9
    r2 = sol.sortedArrayToBST([1])
    assert r2.val == 1 and r2.left is None and r2.right is None
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
