import unittest
import sys
import os

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.restock.priority_list import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
        self.queue = PriorityQueue()
        self.queue.insert(self.item1)
        self.queue.insert(self.item2)

    def test_insert_and_extract(self):
        self.assertEqual(self.queue.extract(), self.item1)
        self.assertEqual(self.queue.extract(), self.item2)

if __name__ == '__main__':
    unittest.main()
