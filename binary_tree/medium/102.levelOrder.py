"""
题目：102. 二叉树的层序遍历 (levelOrder)
难度：中等
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
给你二叉树的根节点 root，返回其节点值的层序遍历。（即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    n15 = TreeNode(15); n7 = TreeNode(7)
    n20 = TreeNode(20, n15, n7); n9 = TreeNode(9)
    n3 = TreeNode(3, n9, n20)
    assert sol.levelOrder(n3) == [[3], [9, 20], [15, 7]]
    assert sol.levelOrder(None) == []
    assert sol.levelOrder(TreeNode(1)) == [[1]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
