"""
题目：25. K 个一组翻转链表 (reverseKGroup)
难度：困难
分类：链表
"""

from typing import List, Optional, Dict, Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ==================== 题目描述 ====================
"""
给你链表的头节点 head，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

示例 2：
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # k=2: 1->2->3->4->5 => 2->1->4->3->5
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3); n4 = ListNode(4); n5 = ListNode(5)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5
    result = sol.reverseKGroup(n1, 2)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [2, 1, 4, 3, 5]
    # k=3
    m1 = ListNode(1); m2 = ListNode(2); m3 = ListNode(3); m4 = ListNode(4); m5 = ListNode(5)
    m1.next = m2; m2.next = m3; m3.next = m4; m4.next = m5
    r = sol.reverseKGroup(m1, 3)
    v = []
    while r:
        v.append(r.val)
        r = r.next
    assert v == [3, 2, 1, 4, 5]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
