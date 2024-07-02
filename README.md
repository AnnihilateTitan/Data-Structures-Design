# Project 5 - Smart Warehouse Management System

## 1.Project Overview
This project revolves around the development of a smart warehouse management system aimed at optimizing the storage, retrieval, and distribution of items within a large warehouse. By leveraging data structures such as linked lists, trees, and heaps, this system ensures efficient and cohesive warehouse management.

## 2.Requirement Analysis of Project

### 2.1 Functional Requirements

#### 2.1.1 Inventory Management
Add Items to Inventory：Support addition of new items containing: unique item ID, name, category, quantity, and priority level.

Remove Items from Inventory：Enable removal of items via item ID, updating the inventory list accordingly.

Update Item Quantities：Allow updates to the quantity of existing items, with validations to ensure non-negative quantities.

Find Items by Name and Category：Provide search functionality for items by name, with additional category-based filtering.

#### 2.1.2 Data Loading

Load Data from CSV：Load initial inventory data from a CSV file, handling any errors gracefully.

Initialize Data Structures：Initialize the linked list for inventory management and a tree for storage optimization upon data loading.

#### 2.1.3 Storage Optimization

Categorize Items：Categorize items into a tree structure, enabling retrieval through category navigation.

Efficient Item Retrieval：Ensure efficient retrieval of items by category and item ID.

#### 2.1.4 Restock Prediction

Identify Low-Quantity Items：Traverse inventory to find items with quantities below a predefined threshold.

Prioritize Restocking：Insert low-quantity items into a priority heap based on their priority level, generating a prioritized restock list.

#### 2.1.5 User Interface

Inventory Management Interface：Provide an interface for adding, removing, and updating items, displaying current inventory details.

Category Tree Visualization：Visualize the category tree, supporting expandable/collapsible nodes.

Restock List Display：Display the restock list, indicating priority levels and current quantities.

### 2.2 Non-Functional Requirements
#### 2.2.1 Performance
Efficient handling of large inventories.

Optimized search and retrieval operations.
#### 2.2.2 Usability
Intuitive, easy-to-use interface with minimal training requirements.

Clear feedback messages for user actions.
#### 2.2.3 Reliability
Ensure data integrity during item operations.

Graceful exception handling with meaningful error messages.
#### 2.2.4 Scalability
Support growth in inventory size and complexity.

Design for scalability with minimal performance degradation.
#### 2.2.5 Maintainability
Well-organized and documented codebase.

Comprehensive unit tests for key functionalities.
#### 2.2.6 Security
Restrict inventory management operations to authorized users.

Implement user authentication and role-based access control.

### 2.3 Optional Features
#### 2.3.1 Interactive Interface
Hover-to-view item details and click-to-remove functionality.
#### 2.3.2 Automated Inventory Adjustment
Automate inventory adjustments based on sales data and trends.
#### 2.3.3Detailed Inventory Reports
Generate reports on inventory levels, restock frequency, and sales performance for informed decision-making.
## 3.Design of Project
### 3.1 Objective
Develop a smart warehouse management system utilizing multiple data structures to manage and optimize storage, retrieval, and distribution of goods.

### 3.2 Detailed Analysis
#### 3.2.1 Defining the Data Structures
（1）Define a Python class for warehouse items, including:

item_ID

name

category (enumeration: ELECTRONICS, FURNITURE, CLOTHING, etc.)

quantity

priority_level (enumeration: HIGH, MEDIUM, LOW)

（2）Implement utility methods:

__repr__: String representation of the item.

__eq__ or __lt__: Comparison based on priority.

（3）Implement a linked list for inventory management:

Each node represents an item:

Item data.

Reference to the next node.
#### 3.2.2Inventory Management Utilities
Implement functions for:

Adding items.

Removing items.

Updating item quantities.

Finding items by name and category.
#### 3.2.3 Loading the Dataset
Implement functions to read data from smart_warehouse_dataset.csv and initialize the data structures.

#### 3.2.4 Optimizing Storage
Organize items by category in a tree structure:

Load items from linked list into category nodes containing linked lists of items.
#### 3.2.5 Predicting Restock Needs
Implement functions to:

Identify low-quantity items.

Insert these items into a heap based on priority.

Extract items to generate a prioritized restock list.
#### 3.2.6 Graphical Interface
Develop an interface for categorized inventory visualization and priority heap management:

Enable operations like adding and removing items.
