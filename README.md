# Mobile Test Automation with Playwright

![CI](https://github.com/kallurayaankit/mobile-test-automation/actions/workflows/ci.yml/badge.svg)

A mobile‑web test suite using **Playwright's built‑in device emulation** (iPhone 13). Tests an e‑commerce site with realistic touch‑screen viewport and mobile‑specific interactions.

## Features
- Real mobile viewport (iPhone 13 profile)
- Page Object Model for reusable page classes
- Parameterized tests driven by JSON data
- Automatic screenshots on failure (just add a hook – see previous projects)
- Parallel execution with pytest-xdist
- CI/CD via GitHub Actions

## Setup (local)

```bash
git clone https://github.com/kallurayaankit/mobile-test-automation.git
cd mobile-test-automation
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
playwright install chromium