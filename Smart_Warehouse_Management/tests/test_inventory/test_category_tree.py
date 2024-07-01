import unittest
import sys
import os

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# 导入需要测试的类
from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.inventory.category_tree import CategoryTree

class TestCategoryTree(unittest.TestCase):

    def setUp(self):
        # 设置测试用例前的初始化工作
        self.item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
        self.item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
        self.tree = CategoryTree()
        self.tree.insert(self.item1.category, self.item1)
        self.tree.insert(self.item2.category, self.item2)

    def test_insert_and_find(self):
        # 测试插入和查找功能
        found_items = self.tree.find_by_category(Category.ELECTRONICS)
        self.assertEqual(found_items.head.item, self.item1)

if __name__ == '__main__':
    unittest.main()