import sys
import os

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from inventory.item import Item, Category
from inventory.linked_list import *

#Initialize a TreeNode with a category.
class TreeNode:
    def __init__(self, category):
        self.category = category
        self.items = LinkedList()  # Initialize a linked list to store items
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node

#Initialize a CategoryTree with a root node set to None.
class CategoryTree:
    def __init__(self):
        self.root = None  # Initialize the root node of the tree

#Insert an item into the category tree.
    def insert(self, category, item):
        
        if self.root is None:
            self.root = TreeNode(category)
            self.root.items.add_item(item)
        else:
            self._insert(self.root, category, item)

#Recursive helper function to insert an item into the category tree.
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

#Find items in the category tree by category.
    def find_by_category(self, category):
        return self._find_by_category(self.root, category)

#Recursive helper function to find items by category in the category tree.
    def _find_by_category(self, node, category):
        
        if node is None:
            return None
        if category.value == node.category.value:
            return node.items
        elif category.value < node.category.value:
            return self._find_by_category(node.left, category)
        else:
            return self._find_by_category(node.right, category)

#Find items in the category tree by item name.
    def find_by_name(self, name):
        
        result = []
        self._find_by_name(self.root, name, result)
        return result

#Recursive helper function to find items by name in the category tree.
    def _find_by_name(self, node, name, result):
        if node is None:
            return
        current = node.items.head
        while current:
            if current.item.name == name:
                result.append(current.item)
            current = current.next
        self._find_by_name(node.left, name, result)
        self._find_by_name(node.right, name, result)

#Find an item in the category tree by item ID.
    def find_by_id(self, item_id):
        return self._find_by_id(self.root, item_id)

#Recursive helper function to find an item by item ID in the category tree.

    def _find_by_id(self, node, item_id):  
        if node is None:
            return None
        current = node.items.head
        while current:
            if current.item.item_ID == item_id:
                return current.item
            current = current.next
        left_result = self._find_by_id(node.left, item_id)
        if left_result:
            return left_result
        return self._find_by_id(node.right, item_id)

#Return a string representation of the category tree.
    def __repr__(self):
        levels = []
        self._traverse_tree(self.root, 0, levels)
        result = []
        for level in levels:
            result.append(" | ".join([repr(node.items) for node in level]))
        return "\n".join(result)

#Recursive helper function to traverse the category tree.
    def _traverse_tree(self, node, depth, levels):
        if node is None:
            return
        if len(levels) == depth:
            levels.append([])
        levels[depth].append(node)
        self._traverse_tree(node.left, depth + 1, levels)
        self._traverse_tree(node.right, depth + 1, levels)
