import time
import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.logic_browser.base_page_app import BasePageApp
from logic.logic_browser.board_page import BoardPage
from logic.logic_browser.home_page import HomePage
from logic.logic_browser.login_page import LoginPage


class TestAddToFavorites(unittest.TestCase):

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

        self.home_page = HomePage(self.driver)

    def tearDown(self) -> None:
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.driver.quit()

    def test_add_board_to_favorites(self):
        # Act
        self.home_page.click_on_the_first_add_to_favorite_button()

        base_page_app = BasePageApp(self.driver)
        base_page_app.click_on_favorite_on_sidebar_button()

        # Assert
        self.assertTrue(base_page_app.check_if_favorite_section_have_board())


if __name__ == '__main__':
    unittest.main()
