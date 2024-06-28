from enum import Enum

# Define an Enum for different categories of items
class Category(Enum):
    ELECTRONICS = 1   
    FURNITURE = 2     
    CLOTHING = 3      

# Define an Enum for different priority levels
class Priority(Enum):
    HIGH = 1    
    MEDIUM = 2  
    LOW = 3    

# Define a class representing an item
class Item:
    def __init__(self, item_ID, name, category, quantity, priority_level):
        self.item_ID = item_ID            
        self.name = name                  
        self.category = category          
        self.quantity = quantity          
        self.priority_level = priority_level  # Priority level of the item

    # Define less than comparison for sorting based on priority level
    def __lt__(self, other):
        return self.priority_level.value < other.priority_level.value

    # String representation of the Item object
    def __repr__(self):
        return (f"Item(item_ID={self.item_ID}, name='{self.name}', "
                f"category={self.category.name}, quantity={self.quantity}, "
                f"priority_level={self.priority_level.name})")
