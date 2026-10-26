from playwright.sync_api import Page
from test_data.users import STANDARD_USER, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_T5_checkout_missing_first_name(page: Page) -> None:
    """T5: Negative test - Checkout with missing first name.

    Precondition:
      standard_user is logged in, on the cart page (/cart.html), and cart has 1 item.
    Steps:
      1. Click the "Checkout" button to proceed to checkout step one.
      2. Leave First Name empty, enter "Doe" in Last Name, and enter "12345" in Zip/Postal Code.
      3. Click "Continue" button.
    Expected result:
      1. After step 1, the URL path is /checkout-step-one.html.
      2. After step 3, the URL path is still /checkout-step-one.html.
      3. After step 3, an error message is visible.
      4. After step 3, the error message text reads "Error: First Name is required".
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Precondition: standard_user is logged in, item in cart, on cart page
    login_page.open()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    inventory_page.wait_for_url_path("/inventory.html")
    inventory_page.add_first_product_to_cart()
    inventory_page.click_cart()
    cart_page.wait_for_url_path("/cart.html")
    assert cart_page.get_items_count() == 1

    # Step 1: Click "Checkout" button
    cart_page.click_checkout()

    # Expected result 1: URL path is /checkout-step-one.html
    checkout_page.wait_for_url_path("/checkout-step-one.html")
    assert checkout_page.get_url_path() == "/checkout-step-one.html"

    # Step 2: Leave First Name empty, fill Last Name and Postal Code
    checkout_page.fill_information(first_name="", last_name="Doe", postal_code="12345")

    # Step 3: Click "Continue" button
    checkout_page.click_continue()

    # Expected result 2: URL path is still /checkout-step-one.html
    assert checkout_page.get_url_path() == "/checkout-step-one.html"

    # Expected result 3: An error message is visible
    assert checkout_page.is_error_visible() is True

    # Expected result 4: The error message text reads "Error: First Name is required"
    assert checkout_page.get_error_text() == "Error: First Name is required"
