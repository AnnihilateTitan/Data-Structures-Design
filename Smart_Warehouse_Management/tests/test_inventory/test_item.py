import unittest
import sys
import os

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将当前脚本文件目录的上级目录添加到系统路径
toolbox_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(toolbox_dir)

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
