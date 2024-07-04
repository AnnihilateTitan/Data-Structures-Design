import tkinter as tk
from tkinter import ttk, messagebox, Menu
import os
import sys
import csv
import datetime
# Get the current script file directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project root directory to the system path
sys.path.append(current_dir)

from project_smart_warehouse_management.toolbox.inventory.item import Item, Category, Priority
from project_smart_warehouse_management.toolbox.restock.priority_list import MinHeap

# This module includes adding data to linked list and loading it into a category tree
from project_smart_warehouse_management.toolbox.utils.loader import *

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
        self.inventorys = load_datasets(self.file_path)
        self.inventory = load_dataset(self.file_path)
        self.restock_queue = predict_restock(self.inventory)

        # Create interface components
        self.create_widgets()
        
        # 创建右键菜单
        self.create_right_click_menu()

    def load_data(self):
        self.inventorys = load_datasets(self.file_path)
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

        # 绑定右键菜单事件
        self.inventory_display.bind("<Button-3>", self.display_right_click_menu)

        self.update_inventory_display()

        # Various function buttons
        tk.Button(self.root, text="Add Item", command=self.open_add_item_window).grid(row=1, column=0, sticky='ew')
        tk.Button(self.root, text="Update Quantity", command=self.open_update_quantity_window).grid(row=1, column=1, sticky='ew')
        tk.Button(self.root, text="Remove Item", command=self.open_remove_item_window).grid(row=2, column=0, sticky='ew')
        tk.Button(self.root, text="Find by Name", command=self.open_find_by_name_window).grid(row=2, column=1, sticky='ew')
        tk.Button(self.root, text="Find by Category", command=self.open_find_by_category_window).grid(row=3, column=0, sticky='ew')
        tk.Button(self.root, text="Find by ID", command=self.open_find_by_id_window).grid(row=3, column=1, sticky='ew')
        tk.Button(self.root, text="Show by Category", command=self.generate_report).grid(row=4, column=1, sticky='ew')
        tk.Button(self.root, text="Generate Restock Queue", command=self.open_restock_threshold_window).grid(row=4, column=0, sticky='ew')
        tk.Button(self.root, text="Log", command=self.show_log).grid(row=5, column=0, columnspan=2, sticky='ew')

    def display_right_click_menu(self, event):
        # 获取右键点击的项目ID
        selected_item = self.inventory_display.selection()
        if selected_item:
            self.selected_item_id = self.inventory_display.item(selected_item)["values"][0]
            self.right_click_menu.post(event.x_root, event.y_root)

    def create_right_click_menu(self):
        # 创建右键菜单
        self.right_click_menu = Menu(self.root, tearoff=False)
        self.right_click_menu.add_command(label="Update Quantity", command=self.open_update_quantity_window_by_right_click)
        self.right_click_menu.add_command(label="Remove Item", command=self.open_remove_item_window_by_right_click)


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
            
    def log_action(self, action_type, item):
        log_file_path = os.path.join(os.path.dirname(__file__), 'files', 'log.txt')
        username = os.getlogin()  # 获取当前登录的用户名
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"{datetime.datetime.now()}: {action_type} - {item} by {username}\n\n")
            
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
                    self.inventorys.insert(category,item)
                    self.inventory.sort_by_id() 
                    self.log_action("Added", item) 
                   

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
                    return True, current.item.quantity, current.item.name
                current = current.next
            return False, None

        def update_quantity():
            try:
                item_id = int(item_id_entry.get())
                new_quantity = int(new_quantity_entry.get())
                exists, original_quantity, item_name= item_exists(item_id)
                if not exists:
                    messagebox.showerror("Error", "No item found with the given ID")
                else:
                    self.inventory.update_quantity(item_id, new_quantity)
                    self.inventorys.update_quantity(item_id, new_quantity)
                    self.log_action("Updated", f"Item {item_name} from {original_quantity} quantity to {new_quantity}")  # Log the action
                    self.update_inventory_display()
                    update_csv_file(self.file_path, self.inventory)  # Update CSV file
                    window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Update", command=update_quantity).grid(row=2, column=0, columnspan=2)

    def open_update_quantity_window_by_right_click(self):
            window = tk.Toplevel(self.root)
            window.title("Update Quantity")

            tk.Label(window, text="New Quantity:").grid(row=1, column=0)
            new_quantity_entry = tk.Entry(window)
            new_quantity_entry.grid(row=1, column=1)

            def item_exists(item_id):
                current = self.inventory.head
                while current:
                    if current.item.item_ID == item_id:
                        return True, current.item.quantity, current.item.name
                    current = current.next
                return False, None

            def update_quantity():
                try:
                    item_id = self.selected_item_id
                    new_quantity = int(new_quantity_entry.get())
                    exists, original_quantity, item_name= item_exists(item_id)
                    if not exists:
                        messagebox.showerror("Error", "No item found with the given ID")
                    else:
                        self.inventory.update_quantity(item_id, new_quantity)
                        self.inventorys.update_quantity(item_id, new_quantity)
                        self.log_action("Updated", f"Item {item_name} from {original_quantity} quantity to {new_quantity}")  # Log the action
                        self.update_inventory_display()
                        update_csv_file(self.file_path, self.inventory)  # Update CSV file
                        window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Invalid input")

            tk.Button(window, text="Update", command=update_quantity).grid(row=2, column=0, columnspan=2)

    def open_remove_item_window(self):
        window = tk.Toplevel(self.root)
        window.title("Remove Item")

        tk.Label(window, text="Item ID:").grid(row=0, column=0)
        item_id_entry = tk.Entry(window)
        item_id_entry.grid(row=0, column=1)

        def item_exists(item_id):
            current = self.inventory.head
            while current:
                if current.item.item_ID == item_id:
                    return current.item
                current = current.next
            return None

        def decrement_ids_above(item_id):
            current = self.inventory.head
            while current:
                if current.item.item_ID > item_id:
                    current.item.item_ID -= 1
                current = current.next

        def remove_item():
            try:
                item_id = int(item_id_entry.get())
                item = item_exists(item_id)
                if not item:
                    messagebox.showerror("Error", "No item found with the given ID")
                else:
                    item_to_log = Item(
                        item_ID=item.item_ID,
                        name=item.name,
                        category=item.category,
                        quantity=item.quantity,
                        priority_level=item.priority_level
                    )

                    if messagebox.askyesno("Confirm Remove", f"Are you sure you want to remove item ID {item_id}?"):
                        self.inventory.remove_item(item_id)
                        self.inventorys.remove(item_id)
                        decrement_ids_above(item_id)
                        self.log_action("Removed", item_to_log)
                        self.update_inventory_display()
                        update_csv_file(self.file_path, self.inventory)  # Update CSV file
                        window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Remove", command=remove_item).grid(row=1, column=0, columnspan=2)

    def open_remove_item_window_by_right_click(self):
        def item_exists(item_id):
            current = self.inventory.head
            while current:
                if current.item.item_ID == item_id:
                    return current.item
                current = current.next
            return None

        def decrement_ids_above(item_id):
            current = self.inventory.head
            while current:
                if current.item.item_ID > item_id:
                    current.item.item_ID -= 1
                current = current.next

        def remove_item():
            try:
                item_id = self.selected_item_id
                item = item_exists(item_id)
                if not item:
                    messagebox.showerror("Error", "No item found with the given ID")
                else:
                    item_to_log = Item(
                        item_ID=item.item_ID,
                        name=item.name,
                        category=item.category,
                        quantity=item.quantity,
                        priority_level=item.priority_level
                    )

                    if messagebox.askyesno("Confirm Remove", f"Are you sure you want to remove item ID {item_id}?"):
                        self.inventory.remove_item(item_id)
                        self.inventorys.remove(item_id)
                        decrement_ids_above(item_id)
                        self.log_action("Removed", item_to_log)
                        self.update_inventory_display()
                        update_csv_file(self.file_path, self.inventory)  # Update CSV file
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        remove_item()


    def open_find_by_name_window(self):
        window = tk.Toplevel(self.root)
        window.title("Find by Name")

        tk.Label(window, text="Name:").grid(row=0, column=0)
        name_entry = tk.Entry(window)
        name_entry.grid(row=0, column=1)

        def find_by_name():
            name = name_entry.get()
            found_items = self.inventorys.find_by_name(name)
            if not found_items:
                messagebox.showinfo("Result", "No items found with the given name")
            else:
                self.display_found_items(found_items)
            window.destroy()

        tk.Button(window, text="Find", command=find_by_name).grid(row=1, column=0, columnspan=2)

    def open_find_by_category_window(self):
        window = tk.Toplevel(self.root)
        window.title("Find by Category")

        tk.Label(window, text="Category:").grid(row=0, column=0)
        category_var = tk.StringVar()
        category_combobox = ttk.Combobox(window, textvariable=category_var)
        category_combobox['values'] = [category.name for category in Category]
        category_combobox.grid(row=0, column=1)

        def find_by_category():
            category = Category[category_var.get().upper()]
            found_items = self.inventorys.find_by_category(category)
            if not found_items:
                messagebox.showinfo("Result", "No items found in the given category")
            else:
                self.display_found_items(found_items)
            window.destroy()

        tk.Button(window, text="Find", command=find_by_category).grid(row=1, column=0, columnspan=2)

    def display_found_items(self, items):
        window = tk.Toplevel(self.root)
        window.title("Found Items")

        found_items_display = ttk.Treeview(window, columns=("ID", "Name", "Category", "Quantity", "Priority"), show="headings")
        found_items_display.heading("ID", text="ID", anchor=tk.W)
        found_items_display.heading("Name", text="Name", anchor=tk.W)
        found_items_display.heading("Category", text="Category", anchor=tk.W)
        found_items_display.heading("Quantity", text="Quantity", anchor=tk.W)
        found_items_display.heading("Priority", text="Priority", anchor=tk.W)
        found_items_display.column("ID", anchor=tk.W, width=50)
        found_items_display.column("Name", anchor=tk.W, width=200)
        found_items_display.column("Category", anchor=tk.W, width=100)
        found_items_display.column("Quantity", anchor=tk.W, width=100)
        found_items_display.column("Priority", anchor=tk.W, width=100)
        found_items_display.grid(row=0, column=0)

        for item in items:
            found_items_display.insert("", tk.END, values=(
                item.item_ID,
                item.name,
                item.category.name,
                item.quantity,
                item.priority_level.name
            ))

    def open_find_by_id_window(self):
        window = tk.Toplevel(self.root)
        window.title("Find by ID")

        tk.Label(window, text="Item ID:").grid(row=0, column=0)
        item_id_entry = tk.Entry(window)
        item_id_entry.grid(row=0, column=1)

        def find_item_by_id():
            try:
                item_id = int(item_id_entry.get())
                item_found = self.inventorys.find_by_id(item_id)

                if item_found:
                    self.display_found_items([item_found])
                    self.update_inventory_display()
                else:
                    messagebox.showerror("Error", f"Item with ID '{item_id}' not found")

            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Find", command=find_item_by_id).grid(row=1, column=0, columnspan=2)

    def open_restock_threshold_window(self):
        window = tk.Toplevel(self.root)
        window.title("Restock Threshold")

        tk.Label(window, text="Restock Threshold:").grid(row=0, column=0)
        threshold_entry = tk.Entry(window)
        threshold_entry.grid(row=0, column=1)
        
        def generate_restock_queue():
            try:
                threshold = int(threshold_entry.get())
                self.restock_queue = predict_restock(self.inventory, threshold)
                self.show_restock_queue()
            except ValueError:
                messagebox.showerror("Error", "Invalid input")
        
        tk.Button(window, text="Generate", command=generate_restock_queue).grid(row=1, column=0, columnspan=2)

    def show_restock_queue(self):
        window = tk.Toplevel(self.root)
        window.title("Restock Queue")

        restock_queue_display = ttk.Treeview(window, columns=("ID", "Name", "Category", "Quantity", "Priority"), show="headings")
        restock_queue_display.heading("ID", text="ID", anchor=tk.W)
        restock_queue_display.heading("Name", text="Name", anchor=tk.W)
        restock_queue_display.heading("Category", text="Category", anchor=tk.W)
        restock_queue_display.heading("Quantity", text="Quantity", anchor=tk.W)
        restock_queue_display.heading("Priority", text="Priority", anchor=tk.W)
        restock_queue_display.column("ID", anchor=tk.W, width=50)
        restock_queue_display.column("Name", anchor=tk.W, width=200)
        restock_queue_display.column("Category", anchor=tk.W, width=100)
        restock_queue_display.column("Quantity", anchor=tk.W, width=100)
        restock_queue_display.column("Priority", anchor=tk.W, width=100)
        restock_queue_display.grid(row=0, column=0)

        while not self.restock_queue.is_empty():
            item = self.restock_queue.extract()
            restock_queue_display.insert("", tk.END, values=(
                item.item_ID,
                item.name,
                item.category.name,
                item.quantity,
                item.priority_level.name
            ))

    def generate_report(self):
            # Create a dictionary to store items categorized by Category
            categorized_items = {}
            current = self.inventory.head
            while current:
                category_name = current.item.category.name
                if category_name not in categorized_items:
                    categorized_items[category_name] = []
                categorized_items[category_name].append((
                    current.item.item_ID,
                    current.item.name,
                    current.item.category.name,
                    current.item.quantity,
                    current.item.priority_level.name
                ))
                current = current.next
            
            # Sort categories alphabetically
            sorted_categories = sorted(categorized_items.keys())

            # Display report sorted by category
            report_data = []
            for category in sorted_categories:
                report_data.extend(categorized_items[category])

            self.show_table_message("Inventory Report", report_data)

    def show_table_message(self, title, data):
        window = tk.Toplevel(self.root)
        window.title(title)

        if isinstance(data, list) and all(isinstance(i, tuple) for i in data):
            tree = ttk.Treeview(window, columns=("ID", "Name", "Category", "Quantity", "Priority"), show="headings")
            tree.heading("ID", text="ID", anchor=tk.W)
            tree.heading("Name", text="Name", anchor=tk.W)
            tree.heading("Category", text="Category", anchor=tk.W)
            tree.heading("Quantity", text="Quantity", anchor=tk.W)
            tree.heading("Priority", text="Priority", anchor=tk.W)
            tree.column("ID", anchor=tk.W, width=50)
            tree.column("Name", anchor=tk.W, width=200)
            tree.column("Category", anchor=tk.W, width=100)
            tree.column("Quantity", anchor=tk.W, width=100)
            tree.column("Priority", anchor=tk.W, width=100)
            tree.grid(row=0, column=0)

            for row in data:
                tree.insert("", tk.END, values=row)
        else:
            tk.Label(window, text=data).grid(row=0, column=0)
            
    def show_log(self):
        log_file_path = os.path.join(os.path.dirname(__file__), 'files', 'log.txt')
        if not os.path.exists(log_file_path):
            messagebox.showinfo("Log", "No log file found.")
            return

        window = tk.Toplevel(self.root)
        window.title("Log")

        text_area = tk.Text(window)
        text_area.pack(expand=True, fill=tk.BOTH)

        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()
            text_area.insert(tk.END, log_content)

        tk.Button(window, text="Close", command=window.destroy).pack()
    
def main():
    root = tk.Tk()
    InventoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

