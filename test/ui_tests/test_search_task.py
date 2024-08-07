import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.logic_browser.base_page_app import BasePageApp
from logic.logic_browser.login_page import LoginPage


class TestSearchTask(unittest.TestCase):

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

        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])

        home_page = BasePageApp(self.driver)
        home_page.click_on_the_board()

    def tearDown(self) -> None:
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()

    def test_search_task_by_name(self):
        """
        Test the search functionality by task name.
        """
        # Arrange


