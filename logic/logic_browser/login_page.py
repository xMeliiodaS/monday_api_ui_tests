from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from infra.browser.base_page import BasePage


class LoginPage(BasePage):
    # ------------------Locators related to the Login------------------
    USERNAME_INPUT = '//input[@id="user_email"]'
    NEXT_BUTTON = "//button[contains(@class, 'next-button')]"
    PASSWORD_INPUT = "//input[@id='user_password']"
    LOGIN_BUTTON = '//button[@aria-label="Log in"]'

    def __init__(self, driver):
        """
        Initialize the LoginPage with a WebDriver instance and set up locators for login elements.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def fill_username_input(self, username):
        """
        Fill in the username input field with the provided username.

        :param username: The username to enter into the email input field.
        """
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.USERNAME_INPUT))).send_keys(username)

    def fill_password_input(self, password):
        """
        Fill in the password input field with the provided password.

        :param password: The password to enter into the password input field.
        """
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT))).send_keys(password)

    def click_on_next_button(self):
        """
        Clicks the 'Next' button after ensuring it's clickable.
        """
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.NEXT_BUTTON))).click()

    def click_on_login_button(self):
        """
        Clicks the 'Log in' button after ensuring it's clickable.
        """
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON))).click()

    def login_flow(self, username, password):
        """
        Executes the login flow using the provided username and password.

        :param username: The username to enter into the email input field.
        :param password: The password to enter into the password input field.
        """
        self.fill_username_input(username)
        self.click_on_next_button()
        self.fill_password_input(password)
        self.click_on_login_button()
