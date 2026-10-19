from playwright.sync_api import Page
from test_data.users import STANDARD_USER, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_T1_login_and_logout(page: Page) -> None:
    """T1: Login and logout.

    Precondition:
      The browser is on the Sauce Demo login page (URL path /).
      No user is logged in.
    Steps:
      1. Enter the username standard_user and the password secret_sauce, and click Login.
      2. Open the burger menu and click Logout.
    Expected result:
      1. After step 1, the URL path is /inventory.html.
      2. After step 1, the page heading reads "Products".
      3. After step 1, the product list contains 6 products.
      4. After step 2, the URL path is /.
      5. After step 2, the Login button is visible.
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # Precondition: browser on login page (/)
    login_page.open()
    assert login_page.get_url_path() == "/"

    # Step 1: Enter credentials and click Login
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    # Expected result 1: URL path is /inventory.html
    inventory_page.wait_for_url_path("/inventory.html")
    assert inventory_page.get_url_path() == "/inventory.html"

    # Expected result 2: Page heading reads "Products"
    assert inventory_page.get_heading_text() == "Products"

    # Expected result 3: Product list contains 6 products
    assert inventory_page.get_product_count() == 6

    # Step 2: Open the burger menu and click Logout
    inventory_page.click_logout()

    # Expected result 4: URL path is /
    login_page.wait_for_url_path("/")
    assert login_page.get_url_path() == "/"

    # Expected result 5: Login button is visible
    login_page.wait_for_login_button()
    assert login_page.is_login_button_visible() is True
