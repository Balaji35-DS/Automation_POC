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

    def enter_username(self, username):
        logger.info("Entering username")
        self.type(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        logger.info("Entering password")
        self.type(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self):
        logger.info("Clicking login button")
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_message(self):
        message = self.get_text(LoginLocators.SUCCESS_MESSAGE)
        logger.info(f"Success message displayed: {message}")
        return message

    def click_logout(self):
        logger.info("Clicking logout")
        self.click(LoginLocators.LOGOUT_BUTTON)
