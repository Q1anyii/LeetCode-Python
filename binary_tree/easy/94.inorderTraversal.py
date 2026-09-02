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
中序遍历顺序：左子树 -> 根节点 -> 右子树
递归思路：
1. 递归终止条件：当前节点为 None，直接返回
2. 递归遍历左子树
3. 将当前节点的值加入结果列表
4. 递归遍历右子树

时间复杂度：O(n)，n为节点个数，每个节点访问一次
空间复杂度：O(n)，最坏情况树退化成链表，递归栈深度为n
"""

# ==================== 代码实现 ====================
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res


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
