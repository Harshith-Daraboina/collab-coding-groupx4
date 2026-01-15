import unittest
from cafe_management.menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()

    def test_add_item(self):
        self.menu.add_item("Brownie", 3.00)
        self.assertIn("Brownie", self.menu.items)
        self.assertEqual(self.menu.items["Brownie"], 3.00)

    def test_remove_item(self):
        self.menu.add_item("Cookie", 1.50)
        self.menu.remove_item("Cookie")
        self.assertNotIn("Cookie", self.menu.items)

    def test_update_item(self):
        self.menu.update_item("Coffee", 3.00)
        self.assertEqual(self.menu.items["Coffee"], 3.00)

if __name__ == '__main__':
    unittest.main()
