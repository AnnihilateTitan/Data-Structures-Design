# Project 5 - Smart Warehouse Management System

## 1.Project Overview

This project revolves around the development of a smart warehouse management system aimed at optimizing the storage, retrieval, and distribution of items within a large warehouse. By leveraging data structures such as linked lists, trees, and heaps, this system ensures efficient and cohesive warehouse management.

## 2.Requirement Analysis of Project

### 2.1 Basic functional

#### 2.1.1 Inventory Management

- **Add Items to Inventory**：Support addition of new items containing: unique item ID, name, category, quantity, and priority level.

- **Remove Items from Inventory**：Enable removal of items via item ID, updating the inventory list accordingly.

- **Update Item Quantities**：Allow updates to the quantity of existing items, with validations to ensure non-negative quantities.

- **Find Items by Name and Category**：Provide search functionality for items by name, with additional category-based filtering.

#### 2.1.2 Data Loading

- **Load Data from CSV**：Load initial inventory data from a CSV file, handling any errors gracefully.

- **Initialize Data Structures**：Initialize the linked list for inventory management and a tree for storage optimization upon data loading.

#### 2.1.3 Storage Optimization

- **Categorize Items**：Categorize items into a tree structure, enabling retrieval through category navigation.

- **Efficient Item Retrieval**：Ensure efficient retrieval of items by category and item ID.

#### 2.1.4 Restock Prediction

- **Identify Low-Quantity Items**：Traverse inventory to find items with quantities below a predefined threshold.

- **Prioritize Restocking**：Insert low-quantity items into a priority heap based on their priority level, generating a prioritized restock list.

#### 2.1.5 User Interface

- **Inventory Management Interface**: Provides an interface for adding, removing, updating, and searching items, displaying current inventory details.

- **Restock List Display**：Display the restock list, indicating priority levels and current quantities.

### 2.2 Extra features

- **Right-click Functionality**: Right-click item in the interface to delete and update his inventory
  
- **Log**: A log button has been added to the interactive interface to make it easy to view the operation of the item

## 3.Design of Project

The data structures we use in the project include linked lists, trees, and heaps. Firstly, we installed extensions to Python, Rainbow CSV, Code Runner, and Coverage Gutters in VsCode.The following image shows our directory file structure:

<p align="center">
    <img src="screenshot/图片1.png" alt="root directory">
</p>

### Linked List

We designed a basic singly linked list supporting:

- Addition
- Removal
- Update
- Sorting
- Iteration

Linked lists offer fast insertion and deletion but slower search and sorting.

### Storage Optimization

To optimize storage, we:

1. Categorized products into a tree by category.
2. Used linked lists to store multiple products under each category.

Recursive operations ensure the efficiency and correctness of the tree structure, enabling rapid search and sorting.

### Tree Structure

Within our tree structure, we implemented some methods:

- Search by ID
- Search by category
- Search by name
- Update item quantity

### Minimum Heap

We implemented a minimum heap to support:

- Insertion
- Extraction of minimum elements
- Checking for emptiness

This facilitates priority queues, task scheduling, and complete replenishment predictions.

### GUI Integration

Finally, we integrated these functionalities into a GUI interface within the main function. Creating a GUI interface using the tkenter library.This interface allows users to:

- Add, delete, modify, and query warehouse items
- Predict replenishments
- Ensure data persistence
- Interact seamlessly via button clicks

This enhances both functionality and user experience.

The following is a screenshot of our designed main interface:

<p align="center">
    <img src="screenshot/屏幕截图 2024-07-04 193133.png" alt="Screenshot of the main interface">
</p>

## 4. Implementation of Project

### 4.1 LinkedList Implementation

This is an implementation of a singly linked list, used for storing and managing items in the warehouse.

#### 4.1.1 Node class

```python
    class Node:
        def __init__(self, item):
            self.item = item 
            self.next = None 
```

Each Node represents a node in the linked list.

Contains two attributes: item (stores an Item object) and next (points to the next node).

#### 4.1.2 LinkedList class

```python
    class LinkedList:
        def __init__(self):
            self.head = None 
```

head: points to the first node of the list.

#### 4.1.3 Main methods in LinkedList class

**(a)add_item(item)**:

```python
    def add_item(self, item):
            new_node = Node(item)   
            new_node.next = self.head   
            self.head = new_node   
```

Creates a new Node object and inserts the new node at the head of the list.

**(b)find_by_id(item_id)**:

```python
    def find_by_id(self, item_id):
        return self._find_by_id(self.root, item_id)

    def _find_by_id(self, node, item_id):  
        if node is None:
            return None
        current = node.items.head
        while current:
            if current.item.item_ID == item_id:
                return current.item
            current = current.next
        left_result = self._find_by_id(node.left, item_id)
        if left_result:
            return left_result
        return self._find_by_id(node.right, item_id)
```

This code implements an efficient item search functionality in a category tree structure using item IDs.

- **Recursive Method:** Utilizes recursion to traverse tree nodes efficiently.

- **Search Strategy:**
  - Begins by checking the item list of the current node.
  - Sequentially searches the left and right subtrees.
  - Stops as soon as a matching item is found or the entire tree has been traversed.

- **Benefits:**
  - Improves search efficiency in large inventory systems.
  - Facilitates quick location of specific items by their IDs without the need to traverse the entire inventory.

**(c)remove_item(item_ID)**:

```python
    def remove_item(self, item_ID):
        current = self.head
        previous = None
        while current and current.item.item_ID != item_ID:
            previous = current
            current = current.next
        if current:   
            if previous:
                previous.next = current.next  
            else:
                self.head = current.next   
```

This code implements the functionality to remove an element with a specified item_ID from a linked list.

- **Traversal:** Iterates through the linked list to find the node matching the item_ID.

- **Node Removal:** Removes the node by adjusting pointers:
  - Updates the previous node's next pointer to skip the node to be removed.
  - Updates the head pointer if the node to be removed is the head node.

- **Structural Integrity:** Ensures that the linked list remains structurally intact after removal.

**(d)update_quantity(item_ID, quantity)**:

```python
    def update_quantity(self, item_ID, quantity):
        current = self.head
        while current:
            if current.item.item_ID == item_ID:
                current.item.quantity = quantity
                return
            current = current.next
```

This code snippet updates the quantity of an item with a specific ID in a linked list.

- **Traversal:** Iterates through the linked list starting from the head node.

- **Item ID Check:** Checks each node’s item ID to find a match with the specified ID.

- **Quantity Update:** When a matching item is found, updates its quantity.

- **Termination:** Terminates the function after updating the quantity of the item.

**(e)sort_by_id()**:

```python
    def sort_by_id(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head
```

This code snippet implements sorting of a linked list based on item IDs using the insertion sort algorithm.

- **Insertion Sort Algorithm:** Iterates through each node of the original list.

- **Sorted Insert:** Inserts each node into the correct position in a new sorted list.

- **Head Update:** Updates the head of the original list to the head of the sorted list after sorting.

- **Completion:** Completes the sorting of the entire linked list based on item IDs.

#### 4.1.4 Advantages of LinkedList

- **Dynamicity:** Elements can be easily added or removed without adjusting the entire data structure.

- **Memory Efficiency:** Memory is allocated only when needed, without pre-allocating large amounts of space.

- **Simple Traversal:** Suitable for operations that require frequent traversal of all items.

- **Application:** Used to store and manage the basic list of all inventory items.
