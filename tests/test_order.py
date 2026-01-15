import unittest
from cafe_management.order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order_mgr = Order()
        self.order = self.order_mgr.create_order()

    def test_create_order(self):
        self.assertEqual(self.order, [])

    def test_add_to_order(self):
        self.order_mgr.add_to_order(self.order, "Burger", 2, 5.0)
        self.assertEqual(len(self.order), 1)
        self.assertEqual(self.order[0]['item'], "Burger")
        self.assertEqual(self.order[0]['quantity'], 2)

if __name__ == '__main__':
    unittest.main()
