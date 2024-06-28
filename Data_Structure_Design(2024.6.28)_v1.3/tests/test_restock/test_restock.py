import unittest
import os
import sys

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.inventory.linked_list import LinkedList
from project_smart_warehouse_management.toolbox.restock.restock import predict_restock

class TestRestock(unittest.TestCase):

    def setUp(self):
        self.item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
        self.inventory = LinkedList()
        self.inventory.add_item(self.item1)
        self.inventory.add_item(self.item2)

    def test_predict_restock(self):
        restock_queue = predict_restock(self.inventory, threshold=6)
        self.assertEqual(restock_queue.extract(), self.item2)

if __name__ == '__main__':
    unittest.main()
