# kaoz-qa-portfolio

A professional QA automation framework built with Python, Playwright, and pytest.

## Stack
- Python 3.12
- Playwright (E2E testing)
- pytest + pytest-html (test runner + reports)
- GitHub Actions (CI/CD) - coming soon

## Structure
- `e2e/` - UI end-to-end tests using Page Object Model
- `api/` - API automation tests
- `reports/` - generated HTML test reports

## Run tests
```bash
python3 -m venv venv
source venv/bin/activate
pip install playwright pytest pytest-playwright pytest-html
playwright install chromium
pytest -v
```