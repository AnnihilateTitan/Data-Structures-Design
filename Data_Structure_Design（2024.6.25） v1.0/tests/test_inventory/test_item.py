import unittest
import sys
import os

# 获取当前文件所在的目录
current_dir = os.path.dirname(__file__)

# 获取项目根目录的路径
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

# 添加项目根目录到sys.path
sys.path.insert(0, project_dir)

# 导入需要测试的类
from project_smart_warehouse_management.inventory.item import Item, Category, Priority

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
