import sys
import os

# Get the directory of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root) to the system path
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from inventory.item import Item

# Class representing a node in the linked list
class Node:
    def __init__(self, item):
        self.item = item  
        self.next = None  

# Class representing the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Head (first node) of the linked list

    # Method to add an item to the linked list
    def add_item(self, item):
        new_node = Node(item)  
        new_node.next = self.head  
        self.head = new_node  

    # Method to remove an item from the linked list by its ID
    def remove_item(self, item_ID):
        current = self.head  
        previous = None  

        # Traverse the list to find the node to remove
        while current and current.item.item_ID != item_ID:
            previous = current
            current = current.next
        if current:
            if previous:  
                previous.next = current.next  # Remove the node by updating the next reference of the previous node
            else:
                self.head = current.next  

    # Method to update the quantity of an item by its ID
    def update_quantity(self, item_ID, quantity):
        current = self.head  # Start from the head of the list
        while current:
            if current.item.item_ID == item_ID:
                current.item.quantity = quantity  # Update the quantity
                return
            current = current.next

    # Method to find items by name
    def find_by_name(self, name):
        result = []  # List to store the matching items
        current = self.head  # Start from the head of the list
        # Traverse the list to find matching items
        while current:
            if current.item.name == name:
                result.append(current.item)
            current = current.next
        return result

    # Method to find items by category
    def find_by_category(self, category):
        result = []  
        current = self.head  
        # Traverse the list to find matching items
        while current:
            if current.item.category == category:
                result.append(current.item)
            current = current.next
        return result

    # Method to represent the linked list as a string
    def __repr__(self):
        items = [] 
        current = self.head  
        while current:
            items.append(repr(current.item))
            current = current.next
        return "->".join(items)  # Join the items with '->' to represent the list
