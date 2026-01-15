import unittest
from unittest.mock import patch
from io import StringIO
from cafe_management.display import Display

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display()

    def test_show_menu(self):
        menu_items = {"Tea": 2.0}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.display.show_menu(menu_items)
            self.assertIn("Tea: $2.00", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
