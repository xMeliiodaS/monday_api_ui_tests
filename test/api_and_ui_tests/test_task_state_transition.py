import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.entites.default_task_payload import DefaultTaskPayload
from logic.enum.section import Section
from logic.logic_api.new_tasks import NewTask
from logic.logic_browser.board_page import BoardPage
from logic.logic_browser.home_page import HomePage
from logic.logic_browser.login_page import LoginPage


class TestTaskStateTransition(unittest.TestCase):

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

        default_task_payload = DefaultTaskPayload()
        new_task = NewTask(self.api_request)

        new_task.post_create_task(default_task_payload.to_dict())

        home_page = HomePage(self.driver)
        home_page.click_on_the_board()

    # ------------------------------------------------------------------------

    def tearDown(self) -> None:
        """
        Clean up after each test case by deleting all tasks and quitting the WebDriver instance.
        """
        self.board_page.delete_all_tasks_from_board()
        self.driver.quit()

    def test_moving_task_to_another_section(self):
        """
        Tests the functionality of moving a task to another section on the board.
        """
        # Arrange
        current_section = Section.NOT_STARTED.value
        target_section = Section.STUCK.value
        self.board_page = BoardPage(self.driver)

        # Verify initial state counts
        initial_not_started_count = self.board_page.get_task_count_in_section(current_section)
        initial_stuck_count = self.board_page.get_task_count_in_section(target_section)

        # Move task from "Not Started" to "Stuck"
        # Act
        self.board_page.move_task_to_another_section(Section.STUCK.value)

        # Verify final state counts
        final_not_started_count = self.board_page.get_task_count_in_section(current_section)
        final_stuck_count = self.board_page.get_task_count_in_section(target_section)

        # Assert
        self.assertEqual(initial_not_started_count - 1, final_not_started_count)
        self.assertEqual(initial_stuck_count + 1, final_stuck_count)
