"""
题目：208. 实现 Trie (前缀树) (Trie)
难度：中等
分类：图
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
Trie（发音类似 "try"）或者说前缀树是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
请你实现 Trie 类：
- Trie() 初始化前缀树对象。
- void insert(String word) 向前缀树中插入字符串 word。
- boolean search(String word) 如果字符串 word 在前缀树中，返回 true；否则，返回 false。
- boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix，返回 true；否则，返回 false。

示例 1：
输入：["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出：[null, null, true, false, true, null, true]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class TrieNode:
    pass
    def __init__(self):
        pass
class Trie:
    pass
    def __init__(self):
        pass
    def insert(self, word: str) -> None:
        pass
    def search(self, word: str) -> bool:
        pass
    def startsWith(self, prefix: str) -> bool:
        pass


# ==================== 测试用例 ====================
def test_solution():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.search("ap") is False
    assert trie.startsWith("ap") is True
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
