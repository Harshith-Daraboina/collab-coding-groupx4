def show_menu(menu):
    print("\n--- Cafe Menu ---")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

def show_bill(order, total):
    print("\n--- Bill Summary ---")
    for item, qty in order.items():
        print(f"{item} x {qty}")
    print(f"Total Amount: ₹{total}")
