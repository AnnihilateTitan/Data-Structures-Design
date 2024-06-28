import os
import sys

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# Import the PriorityQueue class from toolbox.restock.priority_list module
from toolbox.restock.priority_list import PriorityQueue

# Function to predict items that need restocking based on a threshold
def predict_restock(inventory, threshold):
    restock_queue = PriorityQueue()  # Initialize a priority queue for restocking
    current = inventory.head  
    while current:
        if current.item.quantity < threshold:
            restock_queue.insert(current.item)  
        current = current.next  
    return restock_queue 