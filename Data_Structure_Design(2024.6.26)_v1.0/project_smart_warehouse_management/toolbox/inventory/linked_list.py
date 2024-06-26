import sys
import os

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将当前脚本文件目录的上级目录添加到系统路径
toolbox_dir = os.path.dirname(current_dir)
sys.path.append(toolbox_dir)

# 导入自定义模块
from inventory.item import Item

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def remove_item(self, item_ID):
        current = self.head
        previous = None
        while current and current.item.item_ID != item_ID:
            previous = current
            current = current.next
        if current:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def update_quantity(self, item_ID, quantity):
        current = self.head
        while current:
            if current.item.item_ID == item_ID:
                current.item.quantity = quantity
                return
            current = current.next

    def find_by_name(self, name):
        result = []
        current = self.head
        while current:
            if current.item.name == name:
                result.append(current.item)
            current = current.next
        return result

    def find_by_category(self, category):
        result = []
        current = self.head
        while current:
            if current.item.category == category:
                result.append(current.item)
            current = current.next
        return result

    def __repr__(self):
        items = []
        current = self.head
        while current:
            items.append(repr(current.item))
            current = current.next
        return "->".join(items)
