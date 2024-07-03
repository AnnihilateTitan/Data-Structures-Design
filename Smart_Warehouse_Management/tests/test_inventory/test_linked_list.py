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
from project_smart_warehouse_management.toolbox.inventory.linked_list import *




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
        self.assertEqual(self.inventory.head.next.item, self.item1)
        self.assertIsNone(self.inventory.head.next.next)  # Ensure correct linking

    def test_remove_item(self):
        # Test removing an item from the linked list
        self.inventory.remove_item(1)
        self.assertEqual(self.inventory.head.item, self.item2)
        self.assertIsNone(self.inventory.head.next)  # Ensure correct removal

    def test_update_quantity(self):
        # Test updating quantity of an item in the linked list
        self.inventory.update_quantity(1, 15)
        self.assertEqual(self.inventory.head.next.item.quantity, 15)

    def test_sort_by_id(self):
        # Test sorting items by item_ID
        self.inventory.sort_by_id()
        self.assertEqual(self.inventory.head.item, self.item1)
        self.assertEqual(self.inventory.head.next.item, self.item2)

    def test_sorted_insert_empty_list(self):
        # Test inserting into an empty list
        new_item = Item(3, "Desk", Category.FURNITURE, 7, Priority.LOW)
        self.inventory.head = self.inventory.sorted_insert(None, Node(new_item))
        self.assertEqual(self.inventory.head.item, new_item)

    def test_sorted_insert_insert_at_beginning(self):
        # Test inserting at the beginning of a sorted list
        new_item = Item(0, "Mouse", Category.ELECTRONICS, 3, Priority.HIGH)
        self.inventory.head = self.inventory.sorted_insert(self.inventory.head, Node(new_item))
        self.assertEqual(self.inventory.head.item, new_item)
        self.assertEqual(self.inventory.head.next.item, self.item2)

    
    def test_sorted_insert_insert_at_end(self):
        # Test inserting at the end of a sorted list
        new_item = Item(3, "Table", Category.FURNITURE, 8, Priority.LOW)
        self.inventory.head = self.inventory.sorted_insert(self.inventory.head, Node(new_item))
        current = self.inventory.head
        while current.next:
            current = current.next
        self.assertEqual(current.item, new_item)

    def test_iterate_items(self):
        # Test iterating through items using __iter__ method
        items = list(iter(self.inventory))
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0], self.item2)
        self.assertEqual(items[1], self.item1)


if __name__ == '__main__':
    unittest.main()
