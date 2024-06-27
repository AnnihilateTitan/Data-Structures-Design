import unittest
import sys
import os

# Get the directory of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root) to the system path
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# Import classes to be tested
from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.inventory.category_tree import CategoryTree

class TestCategoryTree(unittest.TestCase):

    def setUp(self):
        # Set up initial conditions for the test case
        self.item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
        self.tree = CategoryTree()
        self.tree.insert(self.item1.category, self.item1)
        self.tree.insert(self.item2.category, self.item2)

    def test_insert_and_find(self):
        # Test insertion and finding functionality
        found_items = self.tree.find_by_category(Category.ELECTRONICS)
        self.assertEqual(found_items.head.item, self.item1)

if __name__ == '__main__':
    unittest.main()
