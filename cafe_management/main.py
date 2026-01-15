import sys
from menu import Menu
from order import Order
from billing import Billing
from display import Display

def main():
    menu_mgr = Menu()
    order_mgr = Order()
    billing_mgr = Billing()
    display_mgr = Display()
    
    current_order = order_mgr.create_order()

    while True:
        print("\n=== CAFE MANAGEMENT SYSTEM ===")
        print("1. Show Menu")
        print("2. Add Item to Order")
        print("3. View Current Order")
        print("4. Generate Bill")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_mgr.show_menu(menu_mgr.get_menu())
        
        elif choice == '2':
            display_mgr.show_menu(menu_mgr.get_menu())
            item_name = input("Enter item name: ")
            menu_items = menu_mgr.get_menu()
            
            if item_name in menu_items:
                try:
                    qty = int(input("Enter quantity: "))
                    if qty > 0:
                        order_mgr.add_to_order(current_order, item_name, qty, menu_items[item_name])
                    else:
                        print("Quantity must be positive.")
                except ValueError:
                    print("Invalid quantity.")
            else:
                print("Item not found in menu.")

        elif choice == '3':
            if not current_order:
                print("Order is empty.")
            else:
                print("\n--- Current Order ---")
                for item in current_order:
                    print(f"{item['item']} - Qty: {item['quantity']}")

        elif choice == '4':
            if not current_order:
                print("Order is empty. Cannot generate bill.")
            else:
                billing_mgr.generate_bill(current_order)
                # Reset order after billing? 
                # For this simple version, let's ask or just clear it.
                if input("Start new order? (y/n): ").lower() == 'y':
                    current_order = order_mgr.create_order()
                else:
                    print("Exiting...")
                    break

        elif choice == '5':
            print("Thank you for using Cafe Management System!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
