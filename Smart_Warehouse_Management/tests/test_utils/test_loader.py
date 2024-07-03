import unittest
import sys
import os

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将项目根目录添加到系统路径
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

# 导入需要测试的函数和类
from project_smart_warehouse_management.toolbox.utils.loader import load_dataset
from project_smart_warehouse_management.toolbox.utils.loader import load_datasets
from project_smart_warehouse_management.toolbox.restock.priority_list import MinHeap
from project_smart_warehouse_management.toolbox.inventory.category_tree import *


class TestLoader(unittest.TestCase):

    def test_load_dataset(self):
        # 确保使用正确的文件路径
        file_path = os.path.join(project_dir, 'files', 'smart_warehouse_dataset.csv')
        inventory = load_dataset(file_path)
        self.assertIsNotNone(inventory.head)


    def test_load_datasets(self):
        file_path = os.path.join(project_dir, 'files', 'smart_warehouse_dataset.csv')
        category_tree = load_datasets(file_path)

        self.assertIsInstance(category_tree, CategoryTree)

        # Example: Test finding items by category
        electronics_items = category_tree.find_by_category(Category.ELECTRONICS)
        self.assertIsNotNone(electronics_items)  # Ensure it's not None or empty

        # Example: Test finding items by name
        item_name = 'Laptop'
        laptop_items = category_tree.find_by_name(item_name)
        self.assertIsNotNone(laptop_items)  # Ensure it's not None or empty

        # Test for item with ID 101
        item = category_tree.find_by_id(101)
        self.assertIsNone(item, "Expected item with ID 101 to be None")
if __name__ == '__main__':
    unittest.main()
