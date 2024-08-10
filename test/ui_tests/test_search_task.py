import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.logic_browser.base_page_app import BasePageApp
from logic.logic_browser.board_page import BoardPage
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

        base_page_app = BasePageApp(self.driver)
        base_page_app.click_on_the_board_side_bar_button()

        self.board_page = BoardPage(self.driver)
        self.task_names = Utils.generate_task_names(1)

        self.board_page.create_tasks_with_names(self.task_names)

        self.board_page.click_on_search_button()

    def tearDown(self) -> None:
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        self.board_page.click_on_clear_search()
        self.board_page.delete_all_tasks_from_board()
        self.driver.quit()

    def test_search_task_by_name(self):
        """
        Tests the search functionality by verifying that a task with
         the specified name appears in the search results.
        """
        # Arrange
        task_name = self.task_names[0]

        # Act
        self.board_page.fill_search_input(task_name)
        is_task_appeared = self.board_page.check_if_searched_task_appear(task_name)

        # Assert
        self.assertTrue(is_task_appeared, "The searched task was not found or multiple tasks are displayed.")

    def test_search_task_by_name_negative(self):
        """
        Tests the search functionality by verifying that no tasks
         appear for an incorrect search term.
        """
        # Arrange
        self.board_page.click_on_search_button()

        # Act
        self.board_page.fill_search_input(self.config['incorrect_task_name'])
        is_task_dont_appeared = self.board_page.check_if_searched_task_does_not_appear()

        # Assert
        self.assertTrue(is_task_dont_appeared, "A single tasks are displayed.")


if __name__ == '__main__':
    unittest.main()
