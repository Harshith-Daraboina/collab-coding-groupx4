class Billing:
    def calculate_total(self, order):
        total = 0
        for item in order:
            total += item['price'] * item['quantity']
        return total

    def generate_bill(self, order):
        total = self.calculate_total(order)
        print("\n--- BILL ---")
        for item in order:
            print(f"{item['item']} x {item['quantity']} = ${item['price'] * item['quantity']:.2f}")
        print(f"Total Amount: ${total:.2f}")
        print("------------")
        return total
