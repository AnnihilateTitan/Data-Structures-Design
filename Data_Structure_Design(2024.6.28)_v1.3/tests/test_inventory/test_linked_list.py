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
from project_smart_warehouse_management.toolbox.inventory.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        # Initialize before each test case
        self.item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
        self.inventory = LinkedList()  # Create an instance of LinkedList
        self.inventory.add_item(self.item1) 
        self.inventory.add_item(self.item2)  

    def test_add_item(self):
        # Test adding an item to the linked list
        self.assertEqual(self.inventory.head.item, self.item2) 

    def test_remove_item(self):
        # Test removing an item from the linked list
        self.inventory.remove_item(1)  
        self.assertEqual(self.inventory.head.item, self.item2)  

    def test_update_quantity(self):
        # Test updating quantity of an item in the linked list
        self.inventory.update_quantity(1, 15)  
        self.assertEqual(self.inventory.head.next.item.quantity, 15)  
if __name__ == '__main__':
    unittest.main()
