# Inventory System

A simple Python project that tracks product stock levels, calculates total inventory value, and alerts you when stock is low.

## Files

* **`inventory.py`**: Main code containing product and inventory management classes.
* **`test_inventory.py`**: Test file used to check that everything runs correctly.

## How It Works

* **`Item`**: Stores product info (ID, name, quantity, price) and stops stock from dropping below zero.
* **`InventoryManager`**: Handles adding items, running sales/restocks, and finding low-stock items.

## How to Run Tests

Open your terminal in the project folder and run:

```bash
python -m unittest test_inventory.py -v
