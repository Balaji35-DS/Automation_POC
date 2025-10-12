from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    LOGOUT_BUTTON = (By.XPATH, "(//button[contains (@class, 'btn btn-primary')])[1]")
    ERROR_MESSAGE = (By.ID, "name")
