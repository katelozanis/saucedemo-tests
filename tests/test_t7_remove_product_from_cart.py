from playwright.sync_api import Page, expect
from test_data.users import STANDARD_USER, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_T7_remove_product_from_cart_updates_badge(page: Page) -> None:
    """T7: Own test - Removing a product from cart updates the badge and inventory button state.

    Precondition:
      standard_user is logged in, on the cart page (/cart.html), and the cart lists 1 item.
    Steps:
      1. Click the "Remove" button for the item in the cart.
      2. Click the "Continue Shopping" button.
    Expected result:
      1. After step 1, the cart item is removed and the cart lists 0 items.
      2. After step 1, the cart badge is removed from the header.
      3. After step 2, the URL path is /inventory.html.
      4. After step 2, the first product's button text is "Add to cart".
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # Precondition: standard_user logged in, 1 item added, on cart page
    login_page.open()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    inventory_page.wait_for_url_path("/inventory.html")
    inventory_page.add_first_product_to_cart()
    inventory_page.click_cart()
    cart_page.wait_for_url_path("/cart.html")
    assert cart_page.get_items_count() == 1

    # Step 1: Click the "Remove" button for the item in the cart
    cart_page.remove_first_item()

    # Expected result 1: After step 1, the cart item is removed and the cart lists 0 items
    expect(cart_page.cart_items).to_have_count(0)
    assert cart_page.get_items_count() == 0

    # Expected result 2: After step 1, the cart badge is removed from the header
    assert inventory_page.has_cart_badge() is False

    # Step 2: Click the "Continue Shopping" button
    cart_page.continue_shopping_button.click()

    # Expected result 3: After step 2, the URL path is /inventory.html
    inventory_page.wait_for_url_path("/inventory.html")
    assert inventory_page.get_url_path() == "/inventory.html"

    # Expected result 4: After step 2, the first product's button text is "Add to cart"
    first_item_btn = inventory_page.inventory_items.first.locator("button")
    expect(first_item_btn).to_have_text("Add to cart")
    assert (first_item_btn.text_content() or "").strip() == "Add to cart"
