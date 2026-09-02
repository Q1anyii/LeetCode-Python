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
思路：升序数组是二叉搜索树的中序遍历结果。
要构建高度平衡BST：每次选取数组中间元素作为根节点；
中间左边区间递归构建左子树；中间右边区间递归构建右子树。
1. 递归边界：左边界 > 右边界，返回None
2. 取mid = (left + right) // 2，nums[mid]作为当前根
3. [left, mid‑1] 递归构造左子树
4. [mid+1, right] 递归构造右子树

时间复杂度 O(n)：每个元素构建节点一次
空间复杂度 O(logn)：平衡树递归栈深度；最坏O(n)存树节点
"""

# ==================== 代码实现 ====================
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(nums) - 1)



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
