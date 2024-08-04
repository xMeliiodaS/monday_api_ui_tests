import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.entites.default_task_payload import DefaultTaskPayload
from logic.logic_api.new_task import NewTask
from logic.logic_browser.board_page import BoardPage
from logic.logic_browser.home_page import HomePage
from logic.logic_browser.login_page import LoginPage


class TestCreateDefaultTask(unittest.TestCase):

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

    # ------------------------------------------------------------------------

    def test_post_new_default_task(self):
        # Arrange
        default_task_data = self.config['create_default_task']
        default_task_payload = DefaultTaskPayload(default_task_data['board_id'],
                                                  default_task_data['column_values'], default_task_data['pos'],
                                                  default_task_data['with_undo_data'])
        new_task = NewTask(self.api_request)

        # Create the task
        new_task.post_new_default_task(default_task_payload.to_dict())

        home_page = HomePage(self.driver)
        home_page.click_on_the_board()

        board_page = BoardPage(self.driver)
        self.assertTrue(board_page.is_task_name_displayed(default_task_payload.name))
