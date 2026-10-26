from playwright.sync_api import Page
from test_data.users import PROBLEM_USER, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_T6_problem_user_sort_does_not_reorder(page: Page) -> None:
    """T6: Edge test - problem_user sort does not reorder items.

    Precondition:
      problem_user is logged in and on the inventory page (/inventory.html).
      The sort dropdown has its default option, "Name (A to Z)".
      The page shows 6 products.
    Steps:
      1. Note the names and order of the products on the page.
      2. Attempt to select "Name (Z to A)" in the sort dropdown.
    Expected result:
      1. The selected option of the sort dropdown remains "Name (A to Z)".
      2. The product list still displays items starting with "Sauce Labs Backpack" and maintains the initial order.
      3. The product list still contains 6 products.
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # Precondition: problem_user logged in, on inventory page, 6 products
    login_page.open()
    login_page.login(PROBLEM_USER, STANDARD_PASSWORD)
    inventory_page.wait_for_url_path("/inventory.html")
    assert inventory_page.get_selected_sort_option() == "Name (A to Z)"
    assert inventory_page.get_product_count() == 6

    # Step 1: Note names and order of products on the page
    initial_product_names = inventory_page.get_product_names()
    assert len(initial_product_names) == 6
    assert initial_product_names[0] == "Sauce Labs Backpack"

    # Step 2: Attempt to select "Name (Z to A)" in the sort dropdown
    # In problem_user, the site prevents sorting, so the select option does not change
    inventory_page.sort_dropdown.select_option("za")

    # Expected result 1: The selected option remains "Name (A to Z)"
    assert inventory_page.get_selected_sort_option() == "Name (A to Z)"

    # Expected result 2: The product list maintains the initial order
    current_product_names = inventory_page.get_product_names()
    assert current_product_names == initial_product_names
    assert current_product_names[0] == "Sauce Labs Backpack"

    # Expected result 3: The product list still contains 6 products
    assert inventory_page.get_product_count() == 6
