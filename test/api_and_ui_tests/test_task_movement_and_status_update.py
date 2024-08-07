import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.enum.section import Section
from logic.logic_api.new_tasks import NewTask
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

        new_task = NewTask(self.api_request)
        new_task.post_create_multiple_tasks(6)

        home_page = BasePageApp(self.driver)
        home_page.click_on_the_board_button()

        self.board_page = BoardPage(self.driver)
        self.board_page.move_tasks_to_another_section(Section.WORKING_ON_IT.value, 3)
        self.board_page.move_tasks_to_another_section(Section.STUCK.value, 2)
        self.board_page.move_tasks_to_another_section(Section.DONE.value, 1)
    # ------------------------------------------------------------------------

    def tearDown(self) -> None:
        """
        Clean up after each test case by deleting all tasks and quitting the WebDriver instance.
        """
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
        sections_dict_in_board = self.board_page.get_task_count_in_each_section()

        dashboard_and_reporting = DashboardAndReportingPage(self.driver)
        dashboard_and_reporting.click_on_the_dashboard_and_reporting_button()

        # Act
        sections_dict_in_dashboard = dashboard_and_reporting.get_task_count_in_each_section()

        # Assert
        self.assertDictEqual(sections_dict_in_board, sections_dict_in_dashboard)
