import pytest
from page_objects.login_page import LoginPage
from Test_data.test_data import TestData
from utilities.logger import get_logger

logger = get_logger("UI Negative Tests")


@pytest.mark.ui
def test_invalid_username(driver):
    logger.info("Starting UI Negative test case: Login")
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_username(TestData.INVALID_USERNAME)
    login.enter_password(TestData.VALID_PASSWORD)
    login.click_login()
    # Actual message is "Your username is invalid!"
    assert "You logged into a secure area!" in login.get_message()
    logger.info("Invali username and Login test failed")

@pytest.mark.ui
def test_invalid_password(driver):
    logger.info("Starting UI Negative test case: Invalid password")
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_username(TestData.VALID_USERNAME)
    login.enter_password(TestData.INVALID_PASSWORD)
    login.click_login()
    # Actual message is "Your password is invalid!"
    assert "You logged into a secure area!" in login.get_message()
    logger.info("Invali password and Login test failed")
