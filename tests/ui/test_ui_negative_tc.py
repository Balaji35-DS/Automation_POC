import pytest
from page_objects.login_page import LoginPage
from Test_data.test_data import TestData
from utilities.logger import get_logger

logger = get_logger("UI Negative Tests")


@pytest.mark.ui
def test_invalid_password(driver):
    logger.info("=== Starting Negative Test: Invalid Password ===")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(TestData.VALID_USERNAME, TestData.INVALID_PASSWORD)
    error_msg = login_page.get_error_message()
    assert TestData.ERROR_INVALID_LOGIN in error_msg, f"Unexpected error message: {error_msg}"
    logger.info("Negative login test handled error as expected")

@pytest.mark.ui
def test_invalid_credentials(driver):
    logger.info("=== Starting Negative Test: Empty Credentials ===")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
    error_msg = login_page.get_error_message()
    assert TestData.ERROR_INVALID_LOGIN in error_msg, f"Unexpected error message: {error_msg}"
    logger.info("Negative login test handled error as expected")