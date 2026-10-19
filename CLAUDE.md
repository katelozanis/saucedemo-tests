# Test Automation Standards

Test automation standards for this project:
- Make the smallest change that fixes a problem. No unrelated refactors.
- Test code is production code: small functions, clear names, no copy-paste.
- Use the Page Object pattern (or an equivalent locator layer): one class or module per page. Tests call page methods and never contain locators.
- Locator preference: data-test / test-id attributes, then role or label, then stable CSS. No positional XPath. Look at the real page before choosing locators.
- Wait on conditions (element visible or clickable, URL changed, text present). Never use fixed sleeps or pauses, not even inside helpers. Raise a timeout only with a one-line comment that explains why.
- Each test is independent: it sets up its own state, runs in any order and can run alone.
- One behaviour per test, asserted with a specific expected value, not "the element exists".
- No test retries and no skip/ignore markers on committed tests.
- Configuration comes from environment variables with safe defaults: BASE_URL (default https://www.saucedemo.com/) and HEADLESS (default true; the value "true" means headless). Test data lives in one place. No absolute paths in code or configuration.
- Configure a linter and a formatter, and a pre-commit hook that runs them. Never bypass the hook (--no-verify) and never weaken its configuration to get a commit through.
- After a failing test, show the error and your root-cause hypothesis before changing code.
- Never commit secrets or private data (see the .gitignore in the project).
- Never hand-edit .barko/board/data.json. Never rewrite Git history.
