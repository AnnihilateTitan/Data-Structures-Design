import unittest
import sys
import os

# Get the current directory of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project root directory) to the system path
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)


from project_smart_warehouse_management.toolbox.restock.priority_list import MinHeap



class TestMinHeap(unittest.TestCase):

    def test_insert_and_extract(self):
        heap = MinHeap()
        items = [5, 3, 8, 1, 2]
        
        for item in items:
            heap.insert(item)
        
        sorted_items = []
        while len(heap.heap) > 0:
            sorted_items.append(heap.extract())
        
        self.assertEqual(sorted_items, [1, 2, 3, 5, 8])

    def test_heapify_up(self):
        heap = MinHeap()
        items = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        
        for item in items:
            heap.insert(item)
        
        self.assertEqual(heap.heap[0], 1)

    def test_heapify_down(self):
        heap = MinHeap()
        items = [5, 3, 8, 1, 2]
        
        for item in items:
            heap.insert(item)
        
        self.assertEqual(heap.extract(), 1)
        self.assertEqual(heap.extract(), 2)
        self.assertEqual(heap.extract(), 3)
        self.assertEqual(heap.extract(), 5)
        self.assertEqual(heap.extract(), 8)

    def test_empty_extract(self):
        heap = MinHeap()
        self.assertIsNone(heap.extract())
    
    def test_large_random_insert_and_extract(self):
        import random
        heap = MinHeap()
        items = random.sample(range(1, 1000), 100)
        
        for item in items:
            heap.insert(item)
        
        sorted_items = []
        while len(heap.heap) > 0:
            sorted_items.append(heap.extract())
        
        self.assertEqual(sorted_items, sorted(items))

    def test_initial_empty_heap(self):
        heap = MinHeap()
        self.assertTrue(heap.is_empty())

    def test_repr(self):
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(8)
        self.assertEqual(repr(heap), '[3, 5, 8]')

    

if __name__ == '__main__':
    unittest.main()
