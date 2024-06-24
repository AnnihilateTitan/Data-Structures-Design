from enum import Enum, auto
import unittest

class Category(Enum):
    ELECTRONICS = auto()
    FURNITURE = auto()
    CLOTHING = auto()

class PriorityLevel(Enum):
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

class Item:
    def __init__(self, item_ID, name, category, quantity, priority_level):
        self.item_ID = item_ID
        self.name = name
        self.category = Category[category]
        self.quantity = quantity
        self.priority_level = PriorityLevel[priority_level]

    def __repr__(self):
        return f"Item(ID: {self.item_ID}, Name: {self.name}, Category: {self.category.name}, Quantity: {self.quantity}, Priority: {self.priority_level.name})"

    def __eq__(self, other):
        return self.priority_level == other.priority_level

    def __lt__(self, other):
        return self.priority_level.value < other.priority_level.value

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_item(self, item_ID):
        current = self.head
        previous = None
        while current and current.item.item_ID != item_ID:
            previous = current
            current = current.next
        if not current:
            return False
        if not previous:
            self.head = current.next
        else:
            previous.next = current.next
        return True

    def update_quantity(self, item_ID, new_quantity):
        current = self.head
        while current:
            if current.item.item_ID == item_ID:
                current.item.quantity = new_quantity
                return True
            current = current.next
        return False

    def find_by_name(self, name):
        current = self.head
        result = []
        while current:
            if current.item.name == name:
                result.append(current.item)
            current = current.next
        return result

    def find_by_category(self, category):
        current = self.head
        result = []
        while current:
            if current.item.category == category:
                result.append(current.item)
            current = current.next
        return result

class TestSmartWarehouse(unittest.TestCase):
    def setUp(self):
        self.inventory = LinkedList()
        self.item1 = Item(1, "Laptop", "ELECTRONICS", 10, "HIGH")
        self.item2 = Item(2, "Chair", "FURNITURE", 5, "MEDIUM")
        self.item3 = Item(3, "T-Shirt", "CLOTHING", 20, "LOW")
        self.inventory.add_item(self.item1)
        self.inventory.add_item(self.item2)
        self.inventory.add_item(self.item3)

    def test_add_item(self):
        self.assertEqual(self.inventory.head.item, self.item1)
        self.assertEqual(self.inventory.head.next.item, self.item2)
        self.assertEqual(self.inventory.head.next.next.item, self.item3)

    def test_remove_item(self):
        self.inventory.remove_item(2)
        self.assertIsNone(self.inventory.head.next.item.item_ID == 2)

    def test_update_quantity(self):
        self.inventory.update_quantity(1, 15)
        self.assertEqual(self.inventory.head.item.quantity, 15)

    def test_find_by_name(self):
        result = self.inventory.find_by_name("Laptop")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.item1)

    def test_find_by_category(self):
        result = self.inventory.find_by_category(Category.ELECTRONICS)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.item1)

if __name__ == "__main__":
    unittest.main()