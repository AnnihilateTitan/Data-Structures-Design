import csv
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

from toolbox.inventory.item import Item, Category, Priority
from toolbox.inventory.linked_list import LinkedList

# Function to load dataset from a CSV file
def load_dataset(file_path):
    inventory = LinkedList()  # Initialize a linked list to store the inventory
    with open(file_path, newline='') as csvfile: 
        reader = csv.DictReader(csvfile)  # Create a CSV dictionary reader
        for row in reader:  
            item = Item(
                item_ID=int(row['item_ID']),  # Convert and assign item_ID
                name=row['name'], 
                category=Category[row['category'].upper()],  
                quantity=int(row['quantity']),  
                priority_level=Priority[row['priority_level'].upper()]  
            )
            inventory.add_item(item)  
    return inventory  