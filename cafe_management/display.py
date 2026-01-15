class Display:
    def show_menu(self, menu_items):
        print("\n--- MENU ---")
        for item, price in menu_items.items():
            print(f"{item}: ${price:.2f}")
        print("------------")

    def show_bill(self, order, total):
        # This functionality is partially covered in Billing, but we can separate it if strictly required.
        # For now, let's keep it simple or delegate to this if needed.
        pass
