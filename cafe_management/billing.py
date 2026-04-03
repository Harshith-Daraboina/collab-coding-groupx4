from typing import List, Dict


class Billing:
    def __init__(self, tax_rate: float = 0.0):
        self.tax_rate = tax_rate  # e.g., 0.05 for 5%

    def calculate_subtotal(self, items: List[Dict]) -> float:
        if not items:
            return 0.0

        subtotal = 0.0
        for item in items:
            price = item.get("price", 0)
            quantity = item.get("quantity", 0)

            if price < 0 or quantity < 0:
                raise ValueError("Price and quantity must be non-negative")

            subtotal += price * quantity

        return round(subtotal, 2)

    def apply_discount(self, amount: float, discount: float) -> float:
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100")

        discounted_amount = amount - (amount * discount / 100)
        return round(discounted_amount, 2)

    def apply_tax(self, amount: float) -> float:
        total_with_tax = amount + (amount * self.tax_rate)
        return round(total_with_tax, 2)

    def generate_bill(self, items: List[Dict], discount: float = 0.0) -> Dict:
        subtotal = self.calculate_subtotal(items)
        after_discount = self.apply_discount(subtotal, discount)
        total = self.apply_tax(after_discount)

        return {
            "subtotal": subtotal,
            "discount": discount,
            "tax_rate": self.tax_rate,
            "total": total
        }
