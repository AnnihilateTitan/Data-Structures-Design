import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
import csv

# Get the current script file directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project root directory to the system path
sys.path.append(current_dir)

from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.restock.priority_list import MinHeap
from project_smart_warehouse_management.toolbox.utils.loader import load_dataset
from project_smart_warehouse_management.toolbox.restock.restock import predict_restock

def predict_restock(inventorys, threshold=10):
    restock_queue = MinHeap()
    current = inventorys.head
    while current:
        if current.item.quantity < threshold:
            restock_queue.insert(current.item)
        current = current.next
    return restock_queue

def update_csv_file(file_path, inventory):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['item_ID', 'name', 'category', 'quantity', 'priority_level']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        current = inventory.head
        while current:
            writer.writerow({
                'item_ID': current.item.item_ID,
                'name': current.item.name,
                'category': current.item.category.name,
                'quantity': current.item.quantity,
                'priority_level': current.item.priority_level.name
            })
            current = current.next

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Warehouse Management System")

        # Load dataset
        self.file_path = os.path.join(os.path.dirname(__file__), 'files', 'smart_warehouse_dataset.csv')
        self.inventory = load_dataset(self.file_path)
        self.restock_queue = predict_restock(self.inventory)

        # Create interface components
        self.create_widgets()
        
    def load_data(self):
        self.inventory = load_dataset(self.file_path)
        self.restock_queue = predict_restock(self.inventory)
        
    def update_data(self):
        # Reload data from file
        self.load_data()

        # Update inventory display
        self.update_inventory_display()
        
    def create_widgets(self):
        # Create inventory display frame
        self.inventory_frame = tk.Frame(self.root)
        self.inventory_frame.grid(row=0, column=0, columnspan=2)

        # Create and configure Treeview to display inventory
        self.inventory_display = ttk.Treeview(self.inventory_frame, columns=("ID", "Name", "Category", "Quantity", "Priority"), show="headings")
        self.inventory_display.heading("ID", text="ID", anchor=tk.W)
        self.inventory_display.heading("Name", text="Name", anchor=tk.W)
        self.inventory_display.heading("Category", text="Category", anchor=tk.W)
        self.inventory_display.heading("Quantity", text="Quantity", anchor=tk.W)
        self.inventory_display.heading("Priority", text="Priority", anchor=tk.W)
        self.inventory_display.column("ID", anchor=tk.W, width=50)
        self.inventory_display.column("Name", anchor=tk.W, width=200)
        self.inventory_display.column("Category", anchor=tk.W, width=100)
        self.inventory_display.column("Quantity", anchor=tk.W, width=100)
        self.inventory_display.column("Priority", anchor=tk.W, width=100)
        self.inventory_display.grid(row=0, column=0)

        self.update_inventory_display()

        # Various function buttons
        tk.Button(self.root, text="Add Item", command=self.open_add_item_window).grid(row=1, column=0, sticky='ew')
        tk.Button(self.root, text="Update Quantity", command=self.open_update_quantity_window).grid(row=1, column=1, sticky='ew')

    def update_inventory_display(self):
        for item in self.inventory_display.get_children():
            self.inventory_display.delete(item)
        current = self.inventory.head
        while current:
            self.inventory_display.insert("", tk.END, values=(
                current.item.item_ID,
                current.item.name,
                current.item.category.name,
                current.item.quantity,
                current.item.priority_level.name
            ))
            current = current.next

    def open_add_item_window(self):
        window = tk.Toplevel(self.root)
        window.title("Add Item")

        tk.Label(window, text="Name:").grid(row=0, column=0)
        name_entry = tk.Entry(window)
        name_entry.grid(row=0, column=1)

        tk.Label(window, text="Category:").grid(row=1, column=0)
        category_var = tk.StringVar()
        category_combobox = ttk.Combobox(window, textvariable=category_var)
        category_combobox['values'] = [category.name for category in Category]
        category_combobox.grid(row=1, column=1)

        tk.Label(window, text="Quantity:").grid(row=2, column=0)
        quantity_entry = tk.Entry(window)
        quantity_entry.grid(row=2, column=1)

        tk.Label(window, text="Priority:").grid(row=3, column=0)
        priority_var = tk.StringVar()
        priority_combobox = ttk.Combobox(window, textvariable=priority_var)
        priority_combobox['values'] = [priority.name for priority in Priority]
        priority_combobox.grid(row=3, column=1)

        def get_next_item_id():
            max_id = 0
            current = self.inventory.head
            while current:
                if current.item.item_ID > max_id:
                    max_id = current.item.item_ID
                current = current.next
            return max_id + 1

        def add_item():
            try:
                name = name_entry.get()
                category = Category[category_var.get().upper()]
                quantity = int(quantity_entry.get())
                priority = Priority[priority_var.get().upper()]

                # Check if an item with the same Name, Category, and Priority already exists
                existing_item = None
                current = self.inventory.head
                while current:
                    if current.item.name == name and current.item.category == category and current.item.priority_level == priority:
                        existing_item = current.item
                        break
                    current = current.next

                if existing_item:
                    existing_item.quantity += quantity  # Increment quantity if item already exists
                else:
                    item = Item(
                        item_ID=get_next_item_id(),
                        name=name,
                        category=category,
                        quantity=quantity,
                        priority_level=priority
                    )
                    self.inventory.add_item(item)
                    self.inventory.sort_by_id() 

                self.update_inventory_display()
                update_csv_file(self.file_path, self.inventory)  # Update CSV file
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Add", command=add_item).grid(row=4, column=0, columnspan=2)

    def open_update_quantity_window(self):
        window = tk.Toplevel(self.root)
        window.title("Update Quantity")

        tk.Label(window, text="Item ID:").grid(row=0, column=0)
        item_id_entry = tk.Entry(window)
        item_id_entry.grid(row=0, column=1)

        tk.Label(window, text="New Quantity:").grid(row=1, column=0)
        new_quantity_entry = tk.Entry(window)
        new_quantity_entry.grid(row=1, column=1)

        def item_exists(item_id):
            current = self.inventory.head
            while current:
                if current.item.item_ID == item_id:
                    return True
                current = current.next
            return False

        def update_quantity():
            try:
                item_id = int(item_id_entry.get())
                new_quantity = int(new_quantity_entry.get())
                if not item_exists(item_id):
                    messagebox.showerror("Error", "No item found with the given ID")
                else:
                    self.inventory.update_quantity(item_id, new_quantity)
                    self.update_inventory_display()
                    update_csv_file(self.file_path, self.inventory)  # Update CSV file
                    window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Update", command=update_quantity).grid(row=2, column=0, columnspan=2)

def main():
    root = tk.Tk()
    InventoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
