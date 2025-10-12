import pytest
from page_objects.login_page import LoginPage
from Test_data.test_data import TestData
from utilities.logger import get_logger

logger = get_logger("UI Positive Tests")
@pytest.mark.ui
def test_valid_login(driver):
    logger.info("=== Starting Positive Test: Valid Login ===")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
    assert login_page.is_logout_button_visible(), "Logout button should be visible after successful login"
    logger.info("Valid login test passed")


@pytest.mark.ui
def test_page_title_after_login(driver):
    logger.info("=== Starting Positive Test: Page Title Validation ===")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
    assert TestData.EXPECTED_TITLE in driver.title, "Page title should contain DEMOQA"
    logger.info("Page title validation test passed")
