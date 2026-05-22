import json
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

with open("data/test_data.json") as f:
    products = json.load(f)["products"]

@pytest.fixture
def logged_in_mobile(mobile_page):
    login = LoginPage(mobile_page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    return mobile_page

@pytest.mark.parametrize("product", products)
def test_add_to_cart_mobile(logged_in_mobile, product):
    page = logged_in_mobile
    inventory = InventoryPage(page)
    inventory.add_product_to_cart(product)
    inventory.go_to_cart()
    cart = CartPage(page)
    assert cart.cart_items.filter(has_text=product).count() == 1