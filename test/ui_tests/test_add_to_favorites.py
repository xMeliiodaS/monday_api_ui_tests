import time
import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.logic_browser.base_page_app import BasePageApp
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
        self.is_board_favorited = False

    def tearDown(self) -> None:
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        # Check if the board is in the favorites section
        if self.is_board_favorited:
            self.home_page.toggle_first_favorite_status()

        self.driver.quit()

    def test_add_board_to_favorites(self):
        """
        Tests adding a board to favorites by toggling its favorite status
         and verifying its presence in the favorites section.
        """
        # Act
        self.home_page.toggle_first_favorite_status()

        self.base_page_app = BasePageApp(self.driver)
        self.base_page_app.click_on_favorite_on_sidebar_button()

        # Assert
        self.is_board_favorited = self.base_page_app.check_if_favorite_section_have_board()
        self.assertTrue(self.is_board_favorited,
                        "The board was not added to the favorites section.")

    def test_remove_board_from_favorites(self):
        """
        Tests removing a board from favorites by toggling its favorite status
         and verifying its absence in the favorites section.
        """
        # Act
        # Add the board to favorites
        self.home_page.click_on_the_first_remove_from_favorite_button()

        self.base_page_app = BasePageApp(self.driver)
        self.base_page_app.click_on_favorite_on_sidebar_button()

        # Assert
        # Verify the board is removed
        self.is_board_favorited = self.base_page_app.check_if_favorite_section_have_board()
        self.assertFalse(self.is_board_favorited,
                         "The board is still present in the favorites section after removal.")


if __name__ == '__main__':
    unittest.main()
