import unittest
import os
import sys

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# Import classes and functions to be tested
from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.inventory.linked_list import LinkedList
from project_smart_warehouse_management.toolbox.restock.restock import predict_restock

class TestRestock(unittest.TestCase):

    def setUp(self):
        # Initialize before each test case
        self.item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
        self.inventory = LinkedList()  # Create an instance of LinkedList
        self.inventory.add_item(self.item1)  
        self.inventory.add_item(self.item2)  

    def test_predict_restock(self):
        # Test the predict_restock function
        restock_queue = predict_restock(self.inventory, threshold=6)  
        self.assertEqual(restock_queue.extract(), self.item2)  

if __name__ == '__main__':
    unittest.main()
