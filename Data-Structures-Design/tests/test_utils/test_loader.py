import unittest
import sys
import os

# Get the directory of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root) to the system path
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

# Import the functions and classes to be tested
from project_smart_warehouse_management.toolbox.utils.loader import load_dataset
from project_smart_warehouse_management.toolbox.inventory.item import Category, Priority

class TestLoader(unittest.TestCase):

    def test_load_dataset(self):
        # Ensure using the correct file path
        file_path = os.path.join(project_dir, 'smart_warehouse_dataset.csv')
        inventory = load_dataset(file_path)
        self.assertIsNotNone(inventory.head)

if __name__ == '__main__':
    unittest.main()
