import csv
import sys
import os

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

from toolbox.inventory.item import Item, Category, Priority
from toolbox.inventory.linked_list import LinkedList

def load_dataset(file_path):
    inventory = LinkedList()
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = Item(
                item_ID=int(row['item_ID']),
                name=row['name'],
                category=Category[row['category'].upper()],
                quantity=int(row['quantity']),
                priority_level=Priority[row['priority_level'].upper()]
            )
            inventory.add_item(item)
    return inventory
