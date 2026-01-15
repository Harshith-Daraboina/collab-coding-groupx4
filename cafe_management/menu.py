class Menu:
    def __init__(self):
        # Initial default menu
        self.items = {
            "Coffee": 2.50,
            "Tea": 2.00,
            "Sandwich": 5.00,
            "Cake": 3.50
        }

    def add_item(self, name, price):
        self.items[name] = price
        print(f"Added {name} - ${price}")

    def update_item(self, name, price):
        if name in self.items:
            self.items[name] = price
            print(f"Updated {name} to ${price}")
        else:
            print(f"Item {name} not found.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Removed {name}")
        else:
            print(f"Item {name} not found.")

    def get_menu(self):
        return self.items
