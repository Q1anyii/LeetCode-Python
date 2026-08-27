"""
题目：114. 二叉树展开为链表 (flatten)
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
给你二叉树的根结点 root，请你将它展开为一个单链表：
- 展开后的单链表应该同样使用 TreeNode，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null。
- 展开后的单链表应该与二叉树先序遍历顺序相同。

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    #    1
    #   / \
    #  2   5
    # / \   \
    #3  4    6
    n3 = TreeNode(3); n4 = TreeNode(4)
    n2 = TreeNode(2, n3, n4); n6 = TreeNode(6)
    n5 = TreeNode(5, None, n6); n1 = TreeNode(1, n2, n5)
    sol.flatten(n1)
    vals = []
    curr = n1
    while curr:
        vals.append(curr.val)
        assert curr.left is None
        curr = curr.right
    assert vals == [1, 2, 3, 4, 5, 6]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
