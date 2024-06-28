import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def extract(self):
        return heapq.heappop(self.heap) if self.heap else None

    def __repr__(self):
        return repr(self.heap)
