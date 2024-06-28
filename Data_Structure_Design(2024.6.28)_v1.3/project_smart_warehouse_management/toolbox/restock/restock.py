import os
import sys

# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)


from toolbox.restock.priority_list import PriorityQueue

def predict_restock(inventory, threshold):
    restock_queue = PriorityQueue()
    current = inventory.head
    while current:
        if current.item.quantity < threshold:
            restock_queue.insert(current.item)
        current = current.next
    return restock_queue
