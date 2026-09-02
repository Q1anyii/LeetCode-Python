"""
题目：101. 对称二叉树 (isSymmetric)
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
给你一个二叉树的根节点 root，检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
"""


# ==================== 解题思路 ====================
"""
分左右两边取，
先判断左子树的第一个根节点是否与右子树的第二个节点相同，不相同直接返回false
后续判断left == right and left.left == right.right and left.right == right.left，再依次往下遍历
"""

# ==================== 代码实现 ====================
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(a:TreeNode, b:TreeNode):
            # 两个都为空，对称
            if a is None and b is None:
                return True
            # 一个空一个非空，不对称
            if a is None or b is None:
                return False
            # 值相等 并且 a左 vs b右；a右 vs b左
            return a.val == b.val and dfs(a.left, b.right) and dfs(a.right, b.left)
        if not root:
            return True
        return dfs(root.left, root.right)

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # 对称: 1->(2,2), 2->(3,4), 2->(4,3)
    n3a = TreeNode(3); n4a = TreeNode(4); n4b = TreeNode(4); n3b = TreeNode(3)
    n2a = TreeNode(2, n3a, n4a); n2b = TreeNode(2, n4b, n3b)
    n1 = TreeNode(1, n2a, n2b)
    assert sol.isSymmetric(n1) is True
    # 不对称
    m3a = TreeNode(3); m3b = TreeNode(3)
    m2a = TreeNode(2, None, m3a); m2b = TreeNode(2, None, m3b)
    m1 = TreeNode(1, m2a, m2b)
    assert sol.isSymmetric(m1) is False
    assert sol.isSymmetric(None) is True
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
