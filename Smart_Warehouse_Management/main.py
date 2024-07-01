import os
import sys

# Set the current script file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root) to the system path
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.inventory.linked_list import LinkedList
from project_smart_warehouse_management.toolbox.utils.loader import load_dataset
from project_smart_warehouse_management.toolbox.restock.restock import predict_restock
from project_smart_warehouse_management.toolbox.inventory.category_tree import CategoryTree
# project_smart_warehouse_management/main.py


def main():
    # File path, assuming it's in the 'files' directory
    file_path = os.path.join(os.path.dirname(__file__), 'files', 'smart_warehouse_dataset.csv')

    # Load the dataset
    inventory = LinkedList()
    items = load_dataset(file_path)
    for item in items:
        inventory.add_item(item)

    # Print initial inventory
    print("Initial Inventory:")
    print(inventory)

    # Example of inserting an item
    new_item = Item(item_ID=11, name='Bookshelf', category=Category.FURNITURE, quantity=3, priority_level=Priority.HIGH)
    print("\nInserting item :", new_item)
    inventory.add_item(new_item)
    print("___\nInventory after insertion:")
    print(inventory)

    # Example of removing an item (assuming removing item_ID 3 which is T-Shirt)
    print("\nRemoving item with ID 3")
    inventory.remove_item(3)
    print("___\nInventory after removal:")
    print(inventory)

    # Using CategoryTree to search by category
    category_tree = CategoryTree()
    for item in inventory:
        category_tree.insert(item.category, item)
    
    # Example of searching by category
    print("\nSearching by category ELECTRONICS:")
    electronics_items = category_tree.find_by_category(Category.ELECTRONICS)
    print(electronics_items)

    # Example of searching by name
    print("\nSearching by name Chair:")
    chair_items = category_tree.find_by_name('Chair')
    print(chair_items)

    # Example of searching by item ID
    item_id_to_find = 2  # Change to the item ID you want to search for
    found_item = category_tree.find_by_id(item_id_to_find)
    if found_item:
        print(f"\nItem found with ID {item_id_to_find}:")
        print(found_item)
    else:
        print(f"\nItem with ID {item_id_to_find} not found.")

    # Outputting predicted restock queue
    threshold = 10  # Set the restock threshold
    print(f"\nPredicted restock queue (items below quantity {threshold}):")
    restock_queue = predict_restock(inventory, threshold)
    print(restock_queue)

if __name__ == "__main__":
    main()
