from selenium import webdriver
from config.config import Config
from utilities.logger import get_logger

logger = get_logger("BROWSER_SETUP")

def get_driver():
    try:
        logger.info("Initializing Chrome WebDriver...")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        return driver
    except Exception as e:
        logger.error(f"Error initializing WebDriver: {e}")
        raise
