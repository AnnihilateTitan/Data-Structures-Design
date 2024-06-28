import unittest
import sys
import os

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

# 导入需要测试的函数和类
from project_smart_warehouse_management.toolbox.utils.loader import load_dataset


class TestLoader(unittest.TestCase):

    def test_load_dataset(self):
        # 确保使用正确的路径
        file_path = os.path.join(project_dir, 'smart_warehouse_dataset.csv')
        inventory = load_dataset(file_path)
        self.assertIsNotNone(inventory.head)

if __name__ == '__main__':
    unittest.main()
