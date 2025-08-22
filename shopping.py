# TODO: To write a shopping cart application using dataclass and test it with pytest

from dataclasses import dataclass, field
from typing import List


@dataclass()
class CartItem:
    """
    Represents item in the shopping cart

    Attributes:
        name(str): The name of the item
        quantity(int): number of item want to buy
    """

    name: str
    quantity: int


@dataclass()
class ShoppingCart:
    """
    Gives the ability to add, delete and calculate total ammount from cart
    """

    items: List[CartItem] = field(default_factory=List)
    def add_item():
