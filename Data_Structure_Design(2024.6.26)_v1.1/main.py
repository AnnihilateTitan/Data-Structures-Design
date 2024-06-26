# main.py
import os
import sys

# 获取当前文件所在的目录
current_dir = os.path.dirname(__file__)

# 获取项目根目录的路径
project_dir = os.path.abspath(os.path.join(current_dir))

# 添加项目根目录到sys.path
sys.path.insert(0, project_dir)

from project_smart_warehouse_management.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.inventory.linked_list import LinkedList

def main():
    # 创建一些 Item 实例
    item1 = Item(1, "Laptop", Category.ELECTRONICS, 10, Priority.HIGH)
    item2 = Item(2, "Chair", Category.FURNITURE, 5, Priority.MEDIUM)
    item3 = Item(3, "T-shirt", Category.CLOTHING, 20, Priority.LOW)

    # 创建 LinkedList 实例
    inventory = LinkedList()

    # 添加物品到链表中
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)

    # 打印初始库存
    print("Initial Inventory:")
    print(inventory)

    # 更新物品数量
    inventory.update_quantity(2, 15)
    print("\nInventory after updating Chair quantity to 15:")
    print(inventory)

    # 移除物品
    inventory.remove_item(1)
    print("\nInventory after removing Laptop:")
    print(inventory)

    # 按名称查找物品
    print("\nFind items by name 'Chair':")
    items_by_name = inventory.find_by_name("Chair")
    for item in items_by_name:
        print(item)

    # 按类别查找物品
    print("\nFind items by category CLOTHING:")
    items_by_category = inventory.find_by_category(Category.CLOTHING)
    for item in items_by_category:
        print(item)

if __name__ == '__main__':
    main()
