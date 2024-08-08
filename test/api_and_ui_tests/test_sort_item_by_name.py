import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.logic_api.create_item import CreateItem
from logic.logic_browser.board_page import BoardPage
from logic.logic_browser.base_page_app import BasePageApp
from logic.logic_browser.login_page import LoginPage


class TestSortItemByName(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["login_url"])

        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])

        new_task = CreateItem(self.api_request)
        new_task.post_create_multiple_items(4)

        home_page = BasePageApp(self.driver)
        home_page.click_on_the_board_side_bar_button()

        self.board_page = BoardPage(self.driver)
        self.board_page.choose_sort_flow(self.config['sort_column'])

    # ------------------------------------------------------------------------

    def tearDown(self) -> None:
        """
        Clean up after each test case by deleting all tasks and quitting the WebDriver instance.
        """
#        self.board_page.delete_all_tasks_from_board()
        self.driver.quit()

    # ------------------------------------------------------------------------

    def test_sorting_tasks_by_name(self):
        """
        Tests the functionality of sorting tasks by the 'Name' column and
        verifies that the tasks are sorted in ascending order.
        """
        # Act
        is_sorted_names = self.board_page.check_if_tasks_is_sorted_by_name()

        # Assert
        self.assertTrue(is_sorted_names, "Tasks are not sorted correctly by the 'Name' column")

    def test_sorting_tasks_by_name_negative(self):
        """
        Tests the functionality of invalid sorting tasks by the 'Name' column and
        verifies that the tasks are not sorted in ascending order.
        """
        # Act
        is_unsorted = self.board_page.shuffle_tasks_name()

        # Assert
        self.assertTrue(is_unsorted, "Tasks are still sorted after shuffling.")
