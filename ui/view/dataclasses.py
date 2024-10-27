from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CartItem:
    product_id: int = 0
    variation_id: int = 0
    image: str = ""
    name: str = ""
    quantity: int = 0
    price: float = 0.0
    discount: float = 0.0
    color: str = ""
    size: str = ""
    store_name: str = ""
    
    def get_discounted_price(self):
        """Returns the price after applying the discount, if any."""
        if self.discount > 0:
            return self.price * (1 - (self.discount / 100))
        return self.price

    def get_total_price(self):
        """Returns the total price for the cart item, considering the discount."""
        discounted_price = self.get_discounted_price()
        return discounted_price * self.quantity

@dataclass
class Cart:
    cart_items: Optional[List[CartItem]]
    total: float = 0.0
    discount: float = 0.0
    
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.cart_items)