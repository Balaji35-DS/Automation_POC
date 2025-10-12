# conftest.py
from time import sleep
import time
import pytest
import os
from datetime import datetime
from utilities.logger import get_logger
from utilities.browser_setup import get_driver

logger = get_logger('CONFTST')

@pytest.fixture(scope="session")
def driver():
    logger.info("Initializing WebDriver...")
    driver = get_driver()
    yield driver

    time.sleep(2)
    driver.quit()
    logger.info("WebDriver session ended.")

# ---- Dynamic HTML report filename ----
def pytest_configure(config):
    if not os.path.exists("reports"):
        os.makedirs("reports")
        logger.info("Reports directory created.")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    htmlpath = os.path.join("reports", f"report_{timestamp}.html")
    config.option.htmlpath = htmlpath
    config.option.self_contained_html = True

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    logger.info(f"========== STARTING TEST: {item.name} ==========")

@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    logger.info(f"========== FINISHED TEST: {item.name} ==========")