import sys
import os

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from inventory.item import Item  # Import the Item class from inventory.item module

# Node class represents each node in the linked list
class Node:
    def __init__(self, item):
        self.item = item  # Initialize with an Item object
        self.next = None   # Pointer to the next node in the list

# LinkedList class represents a singly linked list of items
class LinkedList:
    def __init__(self):
        self.head = None   # Initialize an empty linked list

    # Method to add an item to the linked list
    def add_item(self, item):
        new_node = Node(item)   # Create a new node with the given item
        new_node.next = self.head   # Set the new node's next to current head
        self.head = new_node    # Update the head to the new node

    # Method to remove an item from the linked list by item_ID
    def remove_item(self, item_ID):
        current = self.head
        previous = None
        while current and current.item.item_ID != item_ID:
            previous = current
            current = current.next
        if current:   # If item with item_ID found
            if previous:
                previous.next = current.next  # Remove current node by linking previous to next node
            else:
                self.head = current.next   # If the node to be removed is the head

    # Method to update quantity of an item in the linked list by item_ID
    def update_quantity(self, item_ID, quantity):
        current = self.head
        while current:
            if current.item.item_ID == item_ID:
                current.item.quantity = quantity  # Update the quantity of the item
                return
            current = current.next

    # Method to represent the linked list as a string
    def __repr__(self):
        items = []
        current = self.head
        while current:
            items.append(repr(current.item))   # Append string representation of each item
            current = current.next
        return "->".join(items)   # Join item representations with "->" for display

    # Method to iterate over the items in the linked list
    def __iter__(self):
        current = self.head
        while current:
            yield current.item   # Yield each item in the list
            current = current.next
