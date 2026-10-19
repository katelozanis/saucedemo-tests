from playwright.sync_api import Page
from test_data.users import LOCKED_OUT_USER, STANDARD_PASSWORD
from pages.login_page import LoginPage


def test_T4_locked_out_user(page: Page) -> None:
    """T4: Locked-out user.

    Precondition:
      The browser is on the Sauce Demo login page (URL path /).
      No user is logged in.
    Steps:
      1. Enter the username locked_out_user and the password secret_sauce, and click Login.
    Expected result:
      1. The URL path is still /.
      2. The Login button is still visible.
      3. An error message is visible.
      4. The error message text contains "locked out".
    """
    login_page = LoginPage(page)

    # Precondition: browser is on login page (/), no user logged in
    login_page.open()
    assert login_page.get_url_path() == "/"

    # Step 1: Enter username locked_out_user and password secret_sauce, click Login
    login_page.login(LOCKED_OUT_USER, STANDARD_PASSWORD)

    # Expected result 1: URL path is still /
    assert login_page.get_url_path() == "/"

    # Expected result 2: Login button is still visible
    assert login_page.is_login_button_visible() is True

    # Expected result 3: An error message is visible
    assert login_page.is_error_visible() is True

    # Expected result 4: The error message text contains "locked out"
    error_text = login_page.get_error_text()
    assert "locked out" in error_text.lower()
