import json
import pytest
from pages.login_page import LoginPage

with open("data/test_data.json") as f:
    users = json.load(f)["users"]

@pytest.mark.parametrize("user", users, ids=[u["username"] for u in users])
def test_login_mobile(mobile_page, user):
    login_page = LoginPage(mobile_page)
    login_page.navigate()
    login_page.login(user["username"], user["password"])

    if user["valid"]:
        assert mobile_page.url == "https://www.saucedemo.com/inventory.html"
    else:
        assert login_page.error_message.is_visible()