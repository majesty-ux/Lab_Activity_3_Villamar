
import unittest
from inventory import Item, InventoryManager

class TestInventorySystem(unittest.TestCase):
    def setUp(self):
        self.manager =  InventoryManager()
        self.item1 =Item("SKU001", "Keyboard", 15, 89.99, reorder_level=5)
        self.manager.add_item(self.item1)
    def test_stock_reduction(self):
        self.manager.process_transaction("SKU001", -5)
        self.assertEqual(self.item1.quantity, 10)  # Verify stock updated

    def test_insufficient_stock_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.process_transaction("SKU001", -100) # Exceeds quantity of 15