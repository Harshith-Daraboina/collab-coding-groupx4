class Order:
    def __init__(self):
        self.orders = []

    def create_order(self):
        return []

    def add_to_order(self, current_order, item, quantity, price):
        current_order.append({
            "item": item,
            "quantity": quantity,
            "price": price
        })
        print(f"[Order Info] Added {quantity} x {item} to order.")
