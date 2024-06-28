import unittest
import sys
import os

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# Import classes to be tested
from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.restock.priority_list import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        # Initialize before each test case
        self.item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
        self.queue = PriorityQueue()  
        self.queue.insert(self.item1)  
        self.queue.insert(self.item2)  

    def test_insert_and_extract(self):
        # Test insertion and extraction from the priority queue
        self.assertEqual(self.queue.extract(), self.item1)  
        self.assertEqual(self.queue.extract(), self.item2)  

if __name__ == '__main__':
    unittest.main()
