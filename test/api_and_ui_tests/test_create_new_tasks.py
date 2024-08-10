import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.entites.default_item_payload import DefaultItemPayload
from logic.entites.working_on_it_item_payload import WorkingOnItItemPayload
from logic.logic_api.create_item import CreateItem
from logic.logic_browser.board_page import BoardPage
from logic.logic_browser.base_page_app import BasePageApp
from logic.logic_browser.login_page import LoginPage


class TestCreateNewTask(unittest.TestCase):

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

        self.new_task = CreateItem(self.api_request)
        self.base_page_app = BasePageApp(self.driver)

    # ------------------------------------------------------------------------

    def tearDown(self) -> None:
        """
        Clean up after each test case by deleting all tasks and quitting the WebDriver instance.
        """
        self.board_page.delete_all_tasks_from_board()
        self.driver.quit()

    # ------------------------------------------------------------------------

    def test_post_new_default_task(self):
        """
        Tests the creation of a new default task by sending a POST
         request and verifying its appearance on the board.
        """
        default_task_payload = DefaultItemPayload()

        # Act
        self.new_task.post_create_item(default_task_payload)

        self.base_page_app.click_on_the_board_side_bar_button()

        self.board_page = BoardPage(self.driver)

        # Assert
        self.assertTrue(self.board_page.is_task_name_displayed(default_task_payload.name),
                        "The default task is not displayed on the board")

    # ------------------------------------------------------------------------

    def test_post_new_working_on_it_task(self):
        """
        Tests the creation of a new task for the 'working on it' state by
         sending a POST request and verifying its appearance on the board.
        """
        # Arrange
        default_task_payload = WorkingOnItItemPayload()

        # Act
        self.new_task.post_create_working_on_it_item(default_task_payload)

        self.base_page_app.click_on_the_board_side_bar_button()

        self.board_page = BoardPage(self.driver)

        # Assert
        self.assertTrue(self.board_page.is_task_name_displayed(default_task_payload.name),
                        "The 'working on it' task is not displayed on the board")
