import unittest
from cafe_management.billing import Billing

class TestBilling(unittest.TestCase):
    def setUp(self):
        self.billing = Billing()
        self.order = [
            {"item": "Coffee", "quantity": 2, "price": 2.50},
            {"item": "Cake", "quantity": 1, "price": 3.50}
        ]

    def test_calculate_total(self):
        total = self.billing.calculate_total(self.order)
        # 2*2.5 + 1*3.5 = 5 + 3.5 = 8.5
        self.assertEqual(total, 8.50)

if __name__ == '__main__':
    unittest.main()
