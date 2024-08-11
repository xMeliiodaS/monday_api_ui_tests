import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.logic_ui.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes the browser, loads the configuration,
        and navigates to the specified URL.
        """
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["login_url"])

    def tearDown(self) -> None:
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()

    def test_login_successful(self):
        """
        Test the login functionality with valid credentials.
        """
        # Arrange
        login_page = LoginPage(self.driver)

        # Act
        login_page.login_flow(self.config["email"], self.config["password"])

        # Assert
        self.assertTrue(login_page.is_login_successful(), "Login was not successful.")

    def test_login_unsuccessful(self):
        """
        Test the login functionality with invalid credentials.
        """
        # Arrange
        login_page = LoginPage(self.driver)

        # Act
        login_page.login_flow(self.config["email"], self.config["invalid_password"])

        # Assert
        self.assertTrue(login_page.is_login_error_displayed(), "Login error was not displayed.")
