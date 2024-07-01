import csv
import sys
import os

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

# Import Item, Category, and Priority classes from toolbox.inventory.item module
from toolbox.inventory.item import Item, Category, Priority

from project_smart_warehouse_management.toolbox.inventory.category_tree import CategoryTree
# Import LinkedList class from toolbox.inventory.linked_list module
from toolbox.inventory.linked_list import LinkedList

# Function to load dataset from a CSV file into a linked list of items
def load_dataset(file_path):
    inventory = LinkedList()  # Initialize an empty linked list for storing items
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)  
        for row in reader:
            # Create an Item object from each row in the CSV file
            item = Item(
                item_ID=int(row['item_ID']),  
                name=row['name'],             
                category=Category[row['category'].upper()],  
                quantity=int(row['quantity']),  
                priority_level=Priority[row['priority_level'].upper()]  
            )
            inventory.add_item(item) 
    inventory.sort_by_id()
    return inventory  

def load_datasets(file_path):
    inventory = load_dataset(file_path)  # Load data into LinkedList
    inventorys = CategoryTree()  # Initialize CategoryTree

    current = inventory.head
    while current:
        item = current.item
        inventorys.insert(item.category, item)  # Insert item into CategoryTree
        current = current.next
    inventory.sort_by_id()
    return inventorys
