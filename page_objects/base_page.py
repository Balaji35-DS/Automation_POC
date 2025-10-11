from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

logger = get_logger("BASE_PAGE")

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        logger.info(f"Finding element with locator: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        logger.info(f"Element found: {locator}")
        return element

    def click(self, locator):
        logger.info(f"Clicking element: {locator}")
        self.find(locator).click()

    def type(self, locator, text):
        logger.info(f"Typing text into element: {locator}")
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        logger.info(f"Getting text from element: {locator}")
        return self.find(locator).text

    def is_visible(self, locator):
        logger.info(f"Checking visibility of element: {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            logger.info(f"Element is visible: {locator}")
            return True
        except:
            logger.warning(f"Element NOT visible: {locator}")
            return False
