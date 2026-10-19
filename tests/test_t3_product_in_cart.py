from playwright.sync_api import Page
from test_data.users import STANDARD_USER, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_T3_product_in_the_cart(page: Page) -> None:
    """T3: Product in the cart.

    Precondition:
      standard_user is logged in and on the inventory page (/inventory.html).
      The cart is empty (there is no cart badge).
    Steps:
      1. Note the name and price of the first product in the list.
      2. Click "Add to cart" for that product.
      3. Click the cart icon.
    Expected result:
      1. After step 2, the cart badge text is "1".
      2. After step 3, the URL path is /cart.html.
      3. After step 3, the cart lists exactly 1 item.
      4. The cart item's name equals the name noted in step 1.
      5. The cart item's price equals the price noted in step 1, as displayed (e.g. "$29.99").
      6. The cart item's displayed quantity is 1.
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # Precondition: standard_user is logged in on /inventory.html, cart is empty
    login_page.open()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    inventory_page.wait_for_url_path("/inventory.html")
    assert inventory_page.has_cart_badge() is False

    # Step 1: Note the name and price of the first product in the list
    first_product_name = inventory_page.get_first_product_name()
    first_product_price = inventory_page.get_first_product_price()

    # Step 2: Click "Add to cart" for that product
    inventory_page.add_first_product_to_cart()

    # Expected result 1: After step 2, the cart badge text is "1"
    assert inventory_page.get_cart_badge_text() == "1"

    # Step 3: Click the cart icon
    inventory_page.click_cart()

    # Expected result 2: After step 3, the URL path is /cart.html
    cart_page.wait_for_url_path("/cart.html")
    assert cart_page.get_url_path() == "/cart.html"

    # Expected result 3: After step 3, the cart lists exactly 1 item
    assert cart_page.get_items_count() == 1

    # Expected result 4: Cart item's name equals the name noted in step 1
    assert cart_page.get_first_item_name() == first_product_name

    # Expected result 5: Cart item's price equals the price noted in step 1, as displayed
    assert cart_page.get_first_item_price() == first_product_price

    # Expected result 6: Cart item's displayed quantity is 1
    assert cart_page.get_first_item_quantity() == 1
