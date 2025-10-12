import time

from page_objects.base_page import BasePage
from locators.login_locators import LoginLocators
from config.config import Config
from utilities.logger import get_logger

logger = get_logger("LOGIN_PAGE")

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.UI_BASE_URL}/login"

    def open_login_page(self):
        logger.info(f"Opening login page: {self.url}")
        self.driver.get(self.url)

    def login(self, username, password):
        logger.info("Performing login action")
        self.type(LoginLocators.USERNAME_INPUT, username)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        time.sleep(1)
        self.click(LoginLocators.LOGIN_BUTTON)

    def is_logout_button_visible(self):
        logger.info("Checking if logout button is visible")
        return self.is_visible(LoginLocators.LOGOUT_BUTTON)

    def get_error_message(self):
        message = self.get_text(LoginLocators.ERROR_MESSAGE)
        logger.info(f"Success message displayed: {message}")
        return message
