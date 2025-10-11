from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login']/button")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='flash']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")
