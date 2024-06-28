import unittest
import sys
import os

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

# Import the class to be tested
from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority

class TestItem(unittest.TestCase):

    def test_item_creation(self):
        # Test the creation of an Item object
        item = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.assertEqual(item.item_ID, 1)                     
        self.assertEqual(item.name, "Laptop")                 
        self.assertEqual(item.category, Category.ELECTRONICS) 
        self.assertEqual(item.quantity, 10)                   
        self.assertEqual(item.priority_level, Priority.HIGH)  

if __name__ == '__main__':
    unittest.main()
