# 🧪 kaoz-qa-portfolio

A professional QA automation framework built to demonstrate real-world testing skills across UI, API, and CI/CD layers.

![CI Pipeline](https://github.com/siyanda-m2/kaoz-qa-portfolio/actions/workflows/ci.yml/badge.svg)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core language |
| Playwright | End-to-end UI automation |
| pytest | Test runner |
| pytest-html | HTML test reports |
| requests | API automation |
| GitHub Actions | CI/CD pipeline |

---

## 📁 Project Structure
```
kaoz-qa-portfolio/
│
├── e2e/
│   ├── pages/          # Page Object Models
│   └── tests/          # UI test suites
│
├── api/
│   ├── tests/          # API test suites
│   ├── booking_client.py  # Reusable API client
│   └── test_data.py    # Test data definitions
│
├── reports/            # Generated HTML reports
├── .github/workflows/  # CI/CD pipeline
├── conftest.py         # Shared fixtures
└── pytest.ini          # pytest configuration
```

---

## ✅ Test Coverage

### UI Tests — Sauce Demo (saucedemo.com)
- Valid login flow
- Invalid credentials error handling
- Empty credentials validation

### API Tests — Restful Booker API
- GET single booking — status and field validation
- GET all bookings — response structure validation
- POST create booking — payload and response validation
- PUT update booking — data integrity validation
- DELETE booking — deletion and 404 confirmation

---

## 🔄 CI/CD Pipeline

Every push to `main` automatically:
1. Spins up a clean Ubuntu environment
2. Installs all dependencies
3. Installs Playwright browser binaries
4. Runs the full test suite
5. Uploads an HTML report as a build artifact

---

## 🚀 Run Locally
```bash
# Clone the repo
git clone git@github.com:siyanda-m2/kaoz-qa-portfolio.git
cd kaoz-qa-portfolio

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run all tests
pytest -v

# Open the report
# On WSL:
explorer.exe reports/report.html
```

---

## 🧠 Design Decisions

**Page Object Model** — UI tests use POM pattern to separate test logic from page interactions, making tests maintainable and reusable.

**Reusable API Client** — All API interactions are abstracted into a single client class with built-in retry logic and timeouts for CI stability.

**Headless execution** — Tests run headless in CI but can be switched to headed mode locally for debugging.

---

## 📈 Roadmap

- [ ] Add inventory page tests
- [ ] Add checkout flow tests  
- [ ] Integrate Allure reporting
- [ ] Add performance testing with Locust
- [ ] Dockerize the test suite

---

## 👤 Author

**kaoz_dev** — junior automation engineer focused on Python, Playwright, and CI/CD.

🔗 [GitHub](https://github.com/Siyanda-m2)