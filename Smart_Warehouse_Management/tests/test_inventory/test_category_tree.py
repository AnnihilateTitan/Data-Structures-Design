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
        found_items_electronics = self.tree.find_by_category(Category.ELECTRONICS)
        self.assertTrue(found_items_electronics is not None)
        self.assertEqual(found_items_electronics.head.item, self.item1)

        found_items_furniture = self.tree.find_by_category(Category.FURNITURE)
        self.assertTrue(found_items_furniture is not None)
        self.assertEqual(found_items_furniture.head.item, self.item2)

    def test_find_by_name(self):
        # Test finding by name functionality
        found_items = self.tree.find_by_name("Chair")
        self.assertEqual(len(found_items), 1)
        self.assertEqual(found_items[0], self.item2)

    def test_find_by_id(self):
        # Test finding by ID functionality
        found_item = self.tree.find_by_id(1)
        self.assertEqual(found_item, self.item1)

        found_item = self.tree.find_by_id(2)
        self.assertEqual(found_item, self.item2)

    def test_remove(self):
        # Test removing an item by ID
        self.tree.remove(1)
        self.assertIsNone(self.tree.find_by_id(1))

        found_items = self.tree.find_by_category(Category.ELECTRONICS)
        if found_items:
            self.assertNotEqual(found_items.head.item, self.item1)  # Ensure item1 is removed

        self.tree.remove(2)
        self.assertIsNone(self.tree.find_by_id(2))

        found_items = self.tree.find_by_category(Category.FURNITURE)
        if found_items:
            self.assertNotEqual(found_items.head.item, self.item2)  # Ensure item2 is removed

    def test_traverse_tree(self):
        # Test _traverse_tree method to ensure correct traversal
        levels = []
        self.tree._traverse_tree(self.tree.root, 0, levels)

        # Assert the structure of levels matches the expected traversal
        self.assertEqual(len(levels), 2)  # Assuming the tree has two levels
        self.assertEqual(len(levels[0]), 1)  # Root node at level 0
        self.assertEqual(levels[0][0].category, Category.ELECTRONICS)
        self.assertEqual(len(levels[1]), 1)  # Nodes at level 1
        self.assertEqual(levels[1][0].category, Category.FURNITURE)



if __name__ == '__main__':
    unittest.main()
