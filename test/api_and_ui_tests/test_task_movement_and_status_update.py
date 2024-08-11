import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.enum.section import Section
from logic.logic_api.create_item import CreateItem
from logic.logic_browser.board_page import BoardPage
from logic.logic_browser.base_page_app import BasePageApp
from logic.logic_browser.dashboard_and_reporting_page import DashboardAndReportingPage
from logic.logic_browser.login_page import LoginPage


class TestTaskMovementAndStatusUpdate(unittest.TestCase):
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
        new_task.post_create_multiple_default_items(self.config['items_count'])

        base_page_app = BasePageApp(self.driver)
        base_page_app.click_on_the_board_side_bar_button()

        self.board_page = BoardPage(self.driver)
        self.board_page.move_tasks_to_another_sections()

        self.sections_dict_in_board = self.board_page.get_task_count_in_each_section()
        self.dashboard_and_reporting = DashboardAndReportingPage(self.driver)

    # ------------------------------------------------------------------------

    def tearDown(self) -> None:
        """
        Clean up after each test case by deleting all tasks and quitting the WebDriver instance.
        """
        self.dashboard_and_reporting.click_on_the_board_side_bar_button()
        self.board_page.delete_all_tasks_from_board()
        self.driver.quit()

    # ------------------------------------------------------------------------

    def test_task_movement_and_status_update(self):
        """
        Verify that tasks can be moved to different sections and that their status
        is updated correctly.
        Also, ensure that the dashboard reflects the same task counts and statuses
        as the board.
        """
        # Arrange
        self.dashboard_and_reporting.click_on_the_dashboard_and_reporting_button()

        # Act
        sections_dict_in_dashboard = self.dashboard_and_reporting.get_task_count_in_each_section()

        # Assert
        self.assertDictEqual(self.sections_dict_in_board, sections_dict_in_dashboard)

    def test_sum_of_items_in_sections(self):
        """
        Verify that the sum of items in all sections on the board matches the
        sum of items in the 'All Tasks' section on the dashboard.
        """
        # Arrange
        sum_in_board = sum(self.sections_dict_in_board.values())

        self.dashboard_and_reporting.click_on_the_dashboard_and_reporting_button()

        # Act
        sections_dict_in_dashboard = self.dashboard_and_reporting.get_task_count_in_each_section()
        sum_in_dashboard = sum(sections_dict_in_dashboard.values())

        # Assert
        self.assertEqual(sum_in_board, sum_in_dashboard,
                         "The sum of items in the sections on the board does not match the sum on the dashboard.")
