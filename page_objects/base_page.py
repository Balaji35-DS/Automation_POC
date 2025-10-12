from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

logger = get_logger("BASE_PAGE")

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        logger.info(f"Clicking element: {locator}")
        self.find(locator).click()

    def type(self, locator, text):
        logger.info(f"Typing into element:{locator}")
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        text = self.find(locator).text
        logger.info(f"Reading text from element: {locator} -> {text}")
        return text

    def is_visible(self, locator):
        try:
            visible = self.wait.until(EC.visibility_of_element_located(locator))
            logger.info(f"Element visible: {locator}")
            return True if visible else False
        except:
            logger.warning(f"Element not visible: {locator}")
            return False
