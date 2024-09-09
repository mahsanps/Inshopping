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
    
    def get_total_price(self):
        return self.price * self.quantity

@dataclass
class Cart:
    cart_items: Optional[List[CartItem]]
    total: float = 0.0
    discount: float = 0.0
    
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.cart_items)