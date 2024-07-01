import os
import sys

# Get the directory of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root) to the system path
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from inventory.linked_list import LinkedList

#Define a binary search tree
class TreeNode:
    def __init__(self, category):
        self.category = category  # Store the category of the node
        self.items = LinkedList()  # Initialize a linked list to store items in this category
        self.left = None  
        self.right = None  

# Root node of the binary search tree
class CategoryTree:
    def __init__(self):
        self.root = None  

# Insert an item into the tree under the specified category
    def insert(self, category, item): 
        if self.root is None:
            self.root = TreeNode(category)  # If the tree is empty, create the root node
            self.root.items.add_item(item)  # Add the item to the root node's linked list
        else:
            self._insert(self.root, category, item)  # Call the recursive _insert method

# Recursive method to insert an item into the tree
    def _insert(self, node, category, item):        
        if category.value == node.category.value:
            node.items.add_item(item)  # If the category matches, add the item to this node's list
        elif category.value < node.category.value:
            if node.left is None:
                node.left = TreeNode(category)  # If the left child is None, create a new left child
                node.left.items.add_item(item)  # Add the item to the left child's linked list
            else:
                self._insert(node.left, category, item)  # Recur on the left child
        else:
            if node.right is None:
                node.right = TreeNode(category)  
                node.right.items.add_item(item)  
            else:
                self._insert(node.right, category, item)  

# Find and return the linked list of items for the specified category
    def find_by_category(self, category):       
        return self._find_by_category(self.root, category)

# Recursive method to find the linked list of items for the specified category
    def _find_by_category(self, node, category):   
        if node is None:
            return None  # If the node is None, the category is not found
        if category.value == node.category.value:
            return node.items  # If the category matches, return the items linked list
        elif category.value < node.category.value:
            return self._find_by_category(node.left, category)  
        else:
            return self._find_by_category(node.right, category)  

# Generate a string representation of the category tree
    def __repr__(self):       
        levels = []
        self._traverse_tree(self.root, 0, levels)  # Traverse the tree and collect nodes at each level
        result = []
        for level in levels:
            result.append(" | ".join([repr(node.items) for node in level]))  # Join the string representations of the nodes at each level
        return "\n".join(result)

# Recursive method to traverse the tree and collect nodes at each level
    def _traverse_tree(self, node, depth, levels):
        if node is None:
            return
        if len(levels) == depth:
            levels.append([])  # Create a new level in the list if it doesn't exist
        levels[depth].append(node)  # Add the node to the current level
        self._traverse_tree(node.left, depth + 1, levels)  
        self._traverse_tree(node.right, depth + 1, levels)  
