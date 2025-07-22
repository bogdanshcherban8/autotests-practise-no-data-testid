from enum import Enum


class AllureFeature(str, Enum):
    AUTHORIZATION = "Authorization"
    INVENTORY = "Inventory"
    CART = "Cart"
    CHECKOUT = "Checkout"
    SIDEBAR = "SideBar"