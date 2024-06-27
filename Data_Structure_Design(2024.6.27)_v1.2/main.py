# main.py
import os
import sys

# Get the directory of the current script file
current_dir = os.path.dirname(__file__)

# Get the absolute path of the project directory
project_dir = os.path.abspath(os.path.join(current_dir))

# Add the project directory to sys.path
sys.path.insert(0, project_dir)

from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.inventory.linked_list import LinkedList

def main():
    # Create some Item instances
    item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
    item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
    item3 = Item(3, "T-shirt", Category.CLOTHING, 20, Priority.LOW)

    # Create a LinkedList instance
    inventory = LinkedList()

    # Add items to the linked list
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)

    # Print the initial inventory
    print("Initial Inventory:")
    print(inventory)

    # Update the quantity of an item
    inventory.update_quantity(2, 15)
    print("\nInventory after updating Chair quantity to 15:")
    print(inventory)

    # Remove an item
    inventory.remove_item(1)
    print("\nInventory after removing Laptop:")
    print(inventory)

    # Find items by name
    print("\nFind items by name 'Chair':")
    items_by_name = inventory.find_by_name("Chair")
    for item in items_by_name:
        print(item)

    # Find items by category
    print("\nFind items by category CLOTHING:")
    items_by_category = inventory.find_by_category(Category.CLOTHING)
    for item in items_by_category:
        print(item)

if __name__ == '__main__':
    main()
