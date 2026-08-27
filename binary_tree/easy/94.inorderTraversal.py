"""
题目：94. 二叉树的中序遍历 (inorderTraversal)
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
给定一个二叉树的根节点 root，返回它的中序遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pass
        def inorder(node):
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # 1->right 2->left 3
    n3 = TreeNode(3)
    n2 = TreeNode(2, n3, None)
    n1 = TreeNode(1, None, n2)
    assert sol.inorderTraversal(n1) == [1, 3, 2]
    assert sol.inorderTraversal(None) == []
    single = TreeNode(1)
    assert sol.inorderTraversal(single) == [1]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
