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

class TestItem(unittest.TestCase):

    def test_item_creation(self):
        item = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.assertEqual(item.item_ID, 1)
        self.assertEqual(item.name, "Laptop")
        self.assertEqual(item.category, Category.ELECTRONICS)
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.priority_level, Priority.HIGH)

if __name__ == '__main__':
    unittest.main()
