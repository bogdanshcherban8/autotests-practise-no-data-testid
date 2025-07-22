from enum import Enum


class AllureStory(str, Enum):
    LOGIN_FUNCTIONALITY = "Login Functionality"
    INVENTORY_DISPLAY = "Inventory Display"
    CART_MANAGEMENT = "Cart Management"
    ORDER_COMPLETION = 'Order Completion'
    MENU_INTERACTION = "Menu Interaction"
    CHECKOUT_ERRORS = 'Checkout Errors'