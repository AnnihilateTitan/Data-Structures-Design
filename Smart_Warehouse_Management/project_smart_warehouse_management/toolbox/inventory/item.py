from enum import Enum

class Category(Enum):
    ELECTRONICS = 1
    FURNITURE = 2
    CLOTHING = 3

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class Item:
    def __init__(self, item_ID, name, category, quantity, priority_level):
        self.item_ID = item_ID
        self.name = name
        self.category = category
        self.quantity = quantity
        self.priority_level = priority_level

    def __lt__(self, other):
        return self.priority_level.value < other.priority_level.value

    def __repr__(self):
        return (f"Item(item_ID={self.item_ID}, name='{self.name}', "
                f"category={self.category.name}, quantity={self.quantity}, "
                f"priority_level={self.priority_level.name})")
