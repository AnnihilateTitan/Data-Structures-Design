import unittest
import sys
import os

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

# 导入需要测试的类
from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.inventory.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
        self.inventory = LinkedList()
        self.inventory.add_item(self.item1)
        self.inventory.add_item(self.item2)

    def test_add_item(self):
        self.assertEqual(self.inventory.head.item, self.item2)

    def test_remove_item(self):
        self.inventory.remove_item(1)
        self.assertEqual(self.inventory.head.item, self.item2)

    def test_update_quantity(self):
        self.inventory.update_quantity(1, 15)
        self.assertEqual(self.inventory.head.next.item.quantity, 15)

if __name__ == '__main__':
    unittest.main()
