import tkinter as tk

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class FoodItem(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class BeverageItem(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Restaurant:
    def __init__(self):
        self.menu = {
            'foods': [
                FoodItem("Biryani - chicken", 200),
                FoodItem("Biryani - mutton", 250),
                FoodItem("Biryani - Prawns", 300),
                FoodItem("Tandoori - roti - chicken", 250),
                FoodItem("Tandoori - roti - mutton", 300),
                FoodItem("Kadai chicken", 300),
                FoodItem("Boti curry with chapati", 250),
                FoodItem("Egg fried rice with prawns", 150),
                FoodItem("Veg fried rice with pasta and paneer", 150),
                FoodItem("Sire paay with Roti", 300),
                FoodItem("Mutton pulav with nalli nahaari", 500)
            ],
            'sweets': [
                MenuItem("Kaddu ki kheer", 110),
                MenuItem("Kashmiri kheer", 150),
                MenuItem("Mango rabdi", 150),
                MenuItem("Leechee malai", 200),
                MenuItem("Qubani ka meetha", 200),
                MenuItem("Dry and wet fruits icecream malai", 300)
            ],
            'beverages': [
                BeverageItem("Fanta", 60),
                BeverageItem("Goli soda", 20),
                BeverageItem("Limka", 30)
            ]
        }
        self.order = []
        self.total_bill = 0

    def add_to_order(self, item, quantity):
        self.order.append((item, quantity))
        self.total_bill += item.price * quantity

# Function to display the menu
def display_menu(category):
    menu_window = tk.Toplevel(root)
    menu_window.title(f"{category.capitalize()} Menu")

    for i, item in enumerate(restaurant.menu[category], start=1):
        label = tk.Label(menu_window, text=f"{i}. {item.name} - ${item.price}")
        label.pack()

# Function to add item to order
def add_item_to_order(category):
    selection = int(selection_entry.get()) - 1
    quantity = int(quantity_entry.get())

    selected_item = restaurant.menu[category][selection]
    restaurant.add_to_order(selected_item, quantity)

    selection_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# Function to display current order
def display_order():
    order_window = tk.Toplevel(root)
    order_window.title("Current Order")

    for item, quantity in restaurant.order:
        label = tk.Label(order_window, text=f"{item.name} - Quantity: {quantity} - Price: ${item.price * quantity}")
        label.pack()

    total_label = tk.Label(order_window, text=f"Total Bill: ${restaurant.total_bill}")
    total_label.pack()

# Function to print restaurant address
def print_address():
    address_window = tk.Toplevel(root)
    address_window.title("Restaurant Address")

    address_label = tk.Label(address_window, text="5-2-37/19A/1, Fathepura Street, NAVABHARAT\nOpposite TowerCircle, Church road\nPalwancha, Karimnagar-Kothagudem, TS - 505001")
    address_label.pack()

# Create main window
root = tk.Tk()
root.title("Restaurant Menu")

# Set window size and center it on the screen
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Create Restaurant instance
restaurant = Restaurant()

# Create menu buttons
foods_button = tk.Button(root, text="Food Items", command=lambda: display_menu('foods'))
sweets_button = tk.Button(root, text="Sweets and Deserts", command=lambda: display_menu('sweets'))
beverages_button = tk.Button(root, text="Cool Drinks and Beverages", command=lambda: display_menu('beverages'))
order_button = tk.Button(root, text="Display Current Order", command=display_order)
address_button = tk.Button(root, text="Print Restaurant Address", command=print_address)

# Create order entry widgets
selection_label = tk.Label(root, text="Enter the number of the item you'd like to order:")
selection_entry = tk.Entry(root)
quantity_label = tk.Label(root, text="Enter the quantity:")
quantity_entry = tk.Entry(root)

# Create add to order buttons
foods_add_button = tk.Button(root, text="Add Food Item to Order", command=lambda: add_item_to_order('foods'))
sweets_add_button = tk.Button(root, text="Add Sweet Item to Order", command=lambda: add_item_to_order('sweets'))
beverages_add_button = tk.Button(root, text="Add Beverage Item to Order", command=lambda: add_item_to_order('beverages'))

# Place widgets in the main window
foods_button.grid(row=0, column=0, pady=5, padx=10)
sweets_button.grid(row=0, column=1, pady=5, padx=10)
beverages_button.grid(row=0, column=2, pady=5, padx=10)
order_button.grid(row=0, column=3, pady=5, padx=10)
address_button.grid(row=0, column=4, pady=5, padx=10)

selection_label.grid(row=1, column=0, pady=5, padx=10)
selection_entry.grid(row=1, column=1, pady=5, padx=10)
quantity_label.grid(row=1, column=2, pady=5, padx=10)
quantity_entry.grid(row=1, column=3, pady=5, padx=10)

foods_add_button.grid(row=2, column=0, pady=5, padx=10)
sweets_add_button.grid(row=2, column=1, pady=5, padx=10)
beverages_add_button.grid(row=2, column=2, pady=5, padx=10)

root.mainloop()
