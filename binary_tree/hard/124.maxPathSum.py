"""
题目：124. 二叉树中的最大路径和 (maxPathSum)
难度：困难
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
二叉树中的路径被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中至多出现一次。该路径至少包含一个节点，且不一定经过根节点。
路径和是路径中各节点值的总和。
给你一个二叉树的根节点 root，返回其最大路径和。

示例 1：
输入：root = [1,2,3]
输出：6
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass
        def max_gain(node):
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    n2 = TreeNode(2); n3 = TreeNode(3)
    n1 = TreeNode(1, n2, n3)
    assert sol.maxPathSum(n1) == 6
    # 含负数
    m9 = TreeNode(9); m15 = TreeNode(15); m7 = TreeNode(7)
    m20 = TreeNode(20, m15, m7); m_10 = TreeNode(-10, m9, m20)
    assert sol.maxPathSum(m_10) == 42
    assert sol.maxPathSum(TreeNode(-3)) == -3
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
