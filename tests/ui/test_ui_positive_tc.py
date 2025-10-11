import pytest
from page_objects.login_page import LoginPage
from Test_data.test_data import TestData
from utilities.logger import get_logger

logger = get_logger("UI Positive Tests")
@pytest.mark.ui
def test_valid_login(driver):
    logger.info("Starting UI test: Login")
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_username(TestData.VALID_USERNAME)
    login.enter_password(TestData.VALID_PASSWORD)
    login.click_login()
    assert "You logged into a secure area!" in login.get_message()
    logger.info("Login test completed")


@pytest.mark.ui
def test_blank_credentials(driver):
    """Should pass - blank credentials check"""
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_username("")
    login.enter_password("")
    login.click_login()
    assert "Your username is invalid!" in login.get_message()
