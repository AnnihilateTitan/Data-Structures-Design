import heapq  

# PriorityQueue class using heapq to implement a min-heap
class PriorityQueue:
    def __init__(self):
        self.heap = []  # Initialize an empty list to store heap elements

    # Method to insert an item into the priority queue
    def insert(self, item):
        heapq.heappush(self.heap, item)  

    # Method to extract the smallest item (root) from the priority queue
    def extract(self):
        return heapq.heappop(self.heap) if self.heap else None  
    
    # Method to represent the priority queue as a string
    def __repr__(self):
        return repr(self.heap)  # Return the string representation of the heap (list)
