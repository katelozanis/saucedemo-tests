# Sauce Demo UI Test Automation

Automated UI test suite for [Sauce Demo](https://www.saucedemo.com/) developed with Python, Playwright, and pytest following the Page Object Model pattern.

## Installation

Create and activate a virtual environment, then install the pinned dependencies and Playwright browsers:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Running All Tests

To execute all automated tests headless with JUnit XML reporting:

```bash
pytest
```

Reports are automatically generated into `test-results/junit.xml`.

## Running a Single Test

To run a specific test by name (for example, T1):

```bash
pytest -k "test_T1_login_and_logout"
```

Or to run a specific test file:

```bash
pytest tests/test_t1_login_logout.py
```

## Project Organization

The codebase strictly follows the Page Object Model and project hygiene standards:

- `pages/`: Page Object classes encapsulating web elements and interactions. Tests never contain locators directly.
  - `base_page.py`: Base page containing condition-based wait helpers (no fixed `sleep`s).
  - `login_page.py`: Page object for the Sauce Demo login page (`/`).
  - `inventory_page.py`: Page object for the inventory product listing page (`/inventory.html`).
  - `cart_page.py`: Page object for the cart page (`/cart.html`).
  - `checkout_page.py`: Page object for the checkout flow pages.
- `tests/`: Automated test cases implementing the test plan.
  - `conftest.py`: Pytest fixtures managing headless browser and page lifecycle.
- `config/`: Project configuration and environment variable loading (`BASE_URL`, `HEADLESS`).
- `test_data/`: Centralized test fixtures and test account credentials.
- `CLAUDE.md`: Automation standards and architecture rules.
- `.flake8` & `pyproject.toml`: Linter and formatter configurations.

## Environment Variables

The project accepts configuration from environment variables with safe defaults:

- `BASE_URL`: Application base URL (default: `https://www.saucedemo.com/`).
- `HEADLESS`: Browser headless execution flag (default: `true`; setting to `true` runs headless).

You can copy the template `.env.example` to `.env` to override defaults locally:

```bash
cp .env.example .env
```

## Barko audit

The Barko audit was run on the project structure and test automation codebase:

- **High-priority findings:** None detected. All sensitive files (`.env`, `.barko/secrets.local`) are excluded via `.gitignore`, condition-based waits are strictly used instead of fixed sleeps, and all locators reside solely in page objects.
- **Medium-priority findings:**
  - *Finding:* Multi-tab session synchronization check. *Resolution:* Left as-is; out of scope for this assignment as each test runs in an independent browser context.
- **Low-priority findings:**
  - *Finding:* Multi-browser matrix (WebKit and Firefox). *Resolution:* Left as-is; out of scope for this assignment as headless Chromium is specified by the project scope.

