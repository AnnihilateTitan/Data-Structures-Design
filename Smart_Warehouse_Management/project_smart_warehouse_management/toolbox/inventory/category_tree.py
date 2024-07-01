import os
import sys

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from inventory.linked_list import LinkedList

class TreeNode:
    def __init__(self, category):
        self.category = category
        self.items = LinkedList()
        self.left = None
        self.right = None

class CategoryTree:
    def __init__(self):
        self.root = None

    def insert(self, category, item):
        if self.root is None:
            self.root = TreeNode(category)
            self.root.items.add_item(item)
        else:
            self._insert(self.root, category, item)

    def _insert(self, node, category, item):
        if category.value == node.category.value:
            node.items.add_item(item)
        elif category.value < node.category.value:
            if node.left is None:
                node.left = TreeNode(category)
                node.left.items.add_item(item)
            else:
                self._insert(node.left, category, item)
        else:
            if node.right is None:
                node.right = TreeNode(category)
                node.right.items.add_item(item)
            else:
                self._insert(node.right, category, item)

    def find_by_category(self, category):
        return self._find_by_category(self.root, category)

    def _find_by_category(self, node, category):
        if node is None:
            return None
        if category.value == node.category.value:
            return node.items
        elif category.value < node.category.value:
            return self._find_by_category(node.left, category)
        else:
            return self._find_by_category(node.right, category)

    def __repr__(self):
        levels = []
        self._traverse_tree(self.root, 0, levels)
        result = []
        for level in levels:
            result.append(" | ".join([repr(node.items) for node in level]))
        return "\n".join(result)

    def _traverse_tree(self, node, depth, levels):
        if node is None:
            return
        if len(levels) == depth:
            levels.append([])
        levels[depth].append(node)
        self._traverse_tree(node.left, depth + 1, levels)
        self._traverse_tree(node.right, depth + 1, levels)