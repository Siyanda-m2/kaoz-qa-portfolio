# 🧪 kaoz-qa-portfolio

A professional QA automation framework built to demonstrate real-world testing skills across UI, API, and CI/CD layers.

![CI Pipeline](https://github.com/Siyanda-m2/kaoz-qa-portfolio/actions/workflows/ci.yml/badge.svg)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core language |
| Playwright | End-to-end UI automation |
| pytest | Test runner |
| pytest-html | HTML test reports |
| Allure | Professional test reporting dashboard |
| requests | API automation |
| GitHub Actions | CI/CD pipeline |

---

## 📁 Project Structure

```
kaoz-qa-portfolio/
│
├── e2e/
│   ├── pages/                 # Page Object Models
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── tests/                 # UI test suites
│       ├── test_login.py
│       ├── test_inventory.py
│       └── test_checkout.py
│
├── api/
│   ├── tests/                 # API test suites
│   │   └── test_booking_api.py
│   ├── booking_client.py      # Reusable API client with retry logic
│   └── test_data.py           # Test data definitions
│
├── reports/                   # Generated HTML and Allure reports
├── .github/workflows/         # CI/CD pipeline
├── conftest.py                # Shared fixtures + screenshot on failure
└── pytest.ini                 # pytest configuration
```

---

## ✅ Test Coverage

### UI Tests — Sauce Demo (saucedemo.com)

**Login**
- Valid login redirects to inventory
- Invalid credentials shows error message
- Empty credentials shows validation message

**Inventory**
- Page loads 6 products
- Sort by price low to high
- Sort by price high to low
- Sort by name A to Z
- Add single item updates cart badge
- Add multiple items updates cart badge count

**Checkout**
- Full end-to-end checkout flow
- First name required validation
- Last name required validation
- Postal code required validation
- Cart retains correct item

### API Tests — Restful Booker API

- GET single booking — status and field validation
- GET all bookings — response structure validation
- POST create booking — payload and response validation
- PUT update booking — data integrity validation
- DELETE booking — deletion and 404 confirmation
- Auth token generation

---

## 🔄 CI/CD Pipeline

Every push to `main` automatically:
1. Spins up a clean Ubuntu environment
2. Installs all dependencies
3. Installs Playwright browser binaries
4. Runs the full test suite (20 tests)
5. Uploads HTML report as a build artifact
6. Uploads Allure results as a build artifact

---

## 📊 Allure Reporting

Tests are decorated with Allure metadata for professional reporting:

- **Features** — group tests by functional area
- **Stories** — user story level breakdown
- **Severity** — critical, normal, minor classification
- **Screenshots** — automatic capture on test failure
- **Steps** — granular step-by-step execution breakdown

To view the Allure report locally:

```bash
pytest -v
allure generate reports/allure-results -o reports/allure-report --clean
cd reports/allure-report && python3 -m http.server 5050
# Open http://localhost:5050 in your browser
```

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone git@github.com:Siyanda-m2/kaoz-qa-portfolio.git
cd kaoz-qa-portfolio

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run all tests
pytest -v

# Open HTML report (WSL)
explorer.exe reports/report.html
```

---

## 🧠 Design Decisions

**Page Object Model** — UI tests use POM pattern to separate test logic from page interactions, making tests maintainable and reusable as the application grows.

**Reusable API Client** — All API interactions are abstracted into a single client class with built-in retry logic (3 retries, exponential backoff) and 30 second timeouts for CI stability.

**Headless execution** — Tests run headless in CI but can be switched to headed mode locally for debugging by removing the `--browser chromium` flag.

**Screenshot on failure** — conftest.py hooks into pytest to automatically capture and attach a screenshot to the Allure report whenever a UI test fails.

---

## 📈 Roadmap

- [x] Login E2E tests
- [x] Inventory E2E tests
- [x] Checkout E2E tests
- [x] API CRUD tests
- [x] GitHub Actions CI/CD pipeline
- [x] Allure reporting with steps, severity and screenshots
- [ ] Data-driven tests with pytest parametrize
- [ ] Add Allure decorators to all test classes
- [ ] Docker containerization
- [ ] Performance testing with Locust

---

## 👤 Author

**kaoz_dev** — junior automation engineer focused on Python, Playwright, and CI/CD.

🔗 [GitHub](https://github.com/Siyanda-m2)