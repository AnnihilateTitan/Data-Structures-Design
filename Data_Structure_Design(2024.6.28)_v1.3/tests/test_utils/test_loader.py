import unittest
import sys
import os

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

# Import functions and classes to be tested
from project_smart_warehouse_management.toolbox.utils.loader import load_dataset

class TestLoader(unittest.TestCase):

    def test_load_dataset(self):
        # Ensure using the correct file path
        file_path = os.path.join(project_dir, 'smart_warehouse_dataset.csv')
        inventory = load_dataset(file_path)  
        self.assertIsNotNone(inventory.head)  

if __name__ == '__main__':
    unittest.main()
