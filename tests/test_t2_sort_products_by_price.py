from playwright.sync_api import Page
from test_data.users import STANDARD_USER, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_T2_sort_products_by_price(page: Page) -> None:
    """T2: Sort products by price.

    Precondition:
      standard_user is logged in and on the inventory page (/inventory.html).
      The sort dropdown has its default option, "Name (A to Z)".
      The page shows 6 products.
    Steps:
      1. Note the names of the products on the page.
      2. Select "Price (low to high)" in the sort dropdown.
    Expected result:
      1. The selected option of the sort dropdown is "Price (low to high)".
      2. The displayed prices, read as numeric amounts, are in non-decreasing order:
         each price is less than or equal to the next.
      3. The product list still contains 6 products.
      4. The set of product names is the same as the names noted in step 1.
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # Precondition: login as standard_user and navigate to inventory
    login_page.open()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    inventory_page.wait_for_url_path("/inventory.html")
    assert inventory_page.get_selected_sort_option() == "Name (A to Z)"
    assert inventory_page.get_product_count() == 6

    # Step 1: Note the names of the products on the page
    initial_product_names = inventory_page.get_product_names()

    # Step 2: Select "Price (low to high)" in the sort dropdown
    inventory_page.select_sort_option("Price (low to high)")

    # Expected result 1: Selected option is "Price (low to high)"
    assert inventory_page.get_selected_sort_option() == "Price (low to high)"

    # Expected result 2: Prices are in non-decreasing order (p[i] <= p[i+1])
    numeric_prices = inventory_page.get_product_prices_numeric()
    for i in range(len(numeric_prices) - 1):
        assert numeric_prices[i] <= numeric_prices[i + 1]

    # Expected result 3: Product list still contains 6 products
    assert inventory_page.get_product_count() == 6

    # Expected result 4: Set of product names is the same as names noted in step 1
    sorted_product_names = inventory_page.get_product_names()
    assert set(sorted_product_names) == set(initial_product_names)
