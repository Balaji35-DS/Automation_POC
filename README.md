# Automation QA Framework (UI + API) - Chrome & Edge, pytest-html reports

## Overview
This is an Automation QA focused framework (UI + API) built with:
- Selenium (Chrome & Edge)
- Pytest (fixtures, markers)
- Requests (API)
- pytest-xdist (parallel)
- pytest-html (HTML report)

## Folder structure
See the repository layout; key folders:
- `page_objects/` - POM classes
- `locators/` - element locators
- `tests/` - UI & API tests (2 positive + 2 negative each)
- `utilities/` - driver factory, api client, logger
- `test_data/` - JSON test data
- `config/` - environment configs & pytest.ini
- `reports/` & `logs/` - outputs

## Setup
1. create venv: `python -m venv venv`
2. activate venv: mac/linux `source venv/bin/activate` or windows `venv\Scripts\activate`
3. install deps: `pip install -r requirements.txt`

## Run tests examples
- Run UI tests on Chrome (default):
  `pytest -m ui --browser=chrome`
- Run UI tests on Edge:
  `pytest -m ui --browser=edge`
- Run UI tests headless:
  `pytest -m ui --browser=chrome --headless`
- Run API tests:
  `pytest -m api`
- Run all tests in parallel (4 workers):
  `pytest -n 4`
- Generate HTML report (auto-generated to reports/report.html):
  `pytest` (config includes html output)

## Environment selection
- Default env is `dev`. To run against `qa`, pass `--env=qa`:
  `pytest -m api --env=qa`

## Notes
- Screenshots on UI test failures are saved to `reports/screenshots/`.
- WebDriver manager will download browser drivers automatically.
- Do not commit secrets into config files. Use environment variables for sensitive info.
