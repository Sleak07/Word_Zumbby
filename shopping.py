# TODO: To write a shopping cart application using dataclass and test it with pytest

from dataclasses import dataclass, field


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

    items: list[CartItem] = field(default_factory=list)

    def add_item(self, item_name: str, qty: int) -> None:
        """
        Add a specific item to the cart

        Args:
            item_name(str): The name of the item
            qty(int): Quantity of the item to be added to the cart
        """
        self.items.append(CartItem(item_name, qty))

    def remove_item(self, item_name: str) -> None:
        """
        Remove some specific items from cart
        Args:
            item_name(str): The item to be removed
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> int:
        """
        Calculate the total quantity of items in the cart.

        Returns:
            int: The total quantity of all items in the cart.
        """
        return sum(item.quantity for item in self.items)


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Apples", 3)
    cart.add_item("Bananas", 2)
    print("Total qty:", cart.calculate_total())
    cart.remove_item("Apples")
    print("After removal:", cart.calculate_total())
