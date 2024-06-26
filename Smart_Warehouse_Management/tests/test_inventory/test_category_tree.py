import unittest
import sys
import os

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

# Import classes to be tested
from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.inventory.category_tree import CategoryTree

class TestCategoryTree(unittest.TestCase):

    def setUp(self):
        # Initialize before each test case
        self.item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
        self.tree = CategoryTree()
        self.tree.insert(self.item1.category, self.item1)
        self.tree.insert(self.item2.category, self.item2)

    def test_insert_and_find_by_category(self):
        # Test insertion and finding by category functionality
        found_items = self.tree.find_by_category(Category.ELECTRONICS)
        self.assertEqual(found_items.head.item, self.item1)

    def test_find_by_name(self):
        # Test finding by name functionality
        found_items = self.tree.find_by_name("Chair")
        self.assertEqual(len(found_items), 1)
        self.assertEqual(found_items[0], self.item2)

    def test_find_by_id(self):
        # Test finding by ID functionality
        found_item = self.tree.find_by_id(1)
        self.assertEqual(found_item, self.item1)

if __name__ == '__main__':
    unittest.main()
