import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class BillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Retail Store Billing System")

        # Set background image
        self.background_image = ImageTk.PhotoImage(Image.open("C:\Users\shiva\OneDrive\Desktop\DBA_cia\RetailStore.jpg"))
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.pack(fill="both", expand=True)

        # Set background color
        self.root.configure(background="#f0f0f0")

        # Create a dictionary to store product names and prices
        self.products = {
            "Rice": 100,
            "Flour": 200,
            "Sugar": 50,
            "Salt": 50,
            "Oil": 200,
            "Tea": 100,
            "Coffee": 200
        }

        # Create frames for each item
        self.item_frames = []
        for i in range(5):
            frame = tk.Frame(self.root, bg="#f0f0f0")
            frame.pack(fill="x")
            self.item_frames.append(frame)

        # Create labels, comboboxes, and entries for each item
        self.item_labels = []
        self.item_comboboxes = []
        self.item_entries = []
        for i in range(5):
            label = tk.Label(self.item_frames[i], text=f"Item {i+1}:")
            label.pack(side="left")
            self.item_labels.append(label)

            combobox = ttk.Combobox(self.item_frames[i], values=list(self.products.keys()))
            combobox.pack(side="left")
            self.item_comboboxes.append(combobox)

            entry = tk.Entry(self.item_frames[i])
            entry.pack(side="left")
            self.item_entries.append(entry)

        # Create a button to calculate total amount
        self.calculate_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack()

        # Create a label to display total amount
        self.total_label = tk.Label(self.root, text="Total Amount:")
        self.total_label.pack()
        self.total_amount_label = tk.Label(self.root, text="")
        self.total_amount_label.pack()

    def calculate_total(self):
        total_amount = 0
        for i in range(5):
            product_name = self.item_comboboxes[i].get()
            quantity = int(self.item_entries[i].get())
            price = self.products[product_name]
            total_amount += quantity * price
        self.total_amount_label.config(text=f"Rs. {total_amount}")

root = tk.Tk()
billing_system = BillingSystem(root)
root.mainloop()