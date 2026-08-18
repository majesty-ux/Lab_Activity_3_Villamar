class Item: 
    def __init__(self, item_id: str, name:  str, quantity: int, unit_price:  float, reorder_level: int =5 ):
        self.item_id = item_id
        self.name = name
        self.quantity = max(0, quantity)
        self.unit_price = max(0.0, unit_price)
        self.reorder_level = reorder_level

    def update_stock(self, amount: int):
        if self.quantity + amount < 0:
            raise ValueError(f"Cannot fulfill request. Stock is {self.quantity}")
        self.quantity += amount

        @property
        def total_value(self) ->float:
            return self.quantity * self.unit_price

        @property
        def needs_reorder(self) -> bool:
            return self.quantity <= self.reorder_level

class InventoryManager: 
    def __init__(self):
        self._items: dict[str, Item] = {}

    def add_item(self, item: Item ) -> None:
        if item.item_id in self._items: 
            raise ValueError(f"Item with ID {item.item_id} already exists.")
        self._items[item.item_id] = item

    def process_transaction(self, item_id: str, amount: int) -> None:
        if item_id not in self._items:
            raise KeyError("Item not found.")
        self._items[item_id].update_stock(amount)

    def get_low_stock_alerts(self) -> list[Item]:
        return [item for item in self._items.values() if item.needs_reorder]   
