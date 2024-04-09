from __future__ import annotations

from typing import Dict


class Shop:
    def __init__(self, name: str, type: str, capacity: int) -> None:
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items: Dict[str, int] = {}

    @classmethod
    def small_shop(cls, name: str, type: str) -> Shop:
        return cls(name, type, 10)

    def add_item(self, item_name: str) -> str:
        if self.capacity > 0:
            if item_name not in self.items.keys():
                self.items[item_name] = 0
            self.items[item_name] += 1
            self.capacity -= 1
            return f'{item_name} added to the shop'
        return 'Not enough capacity in the shop'

    def remove_item(self, item_name: str, amount: int) -> str:
        err = f'Cannot remove {amount} {item_name}'

        if item_name not in self.items.keys():
            return err

        if amount > self.items[item_name]:
            return err

        self.items[item_name] -= amount
        self.capacity += amount

        if self.items[item_name] == 0:
            del self.items[item_name]

        return f'{amount} {item_name} removed from the shop'

    def __repr__(self) -> str:
        return f'{self.name} of type {self.type} with capacity {self.capacity}'
