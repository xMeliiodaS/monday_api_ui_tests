import time
import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.logic_browser.base_page_app import BasePageApp
from logic.logic_browser.board_page import BoardPage
from logic.logic_browser.login_page import LoginPage


class TestUpdateTask(unittest.TestCase):

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

    def tearDown(self) -> None:
        """
        Clean up after each test case by quitting the WebDriver instance.
        """
        #   self.board_page.delete_all_tasks_from_board()
        self.driver.quit()

    def test_update_task_name(self):
        """
        Test the search functionality by task name.
        """
        # Arrange
        task_name = self.task_names[0]
        generated_new_task_name = Utils.generate_task_names(1)

        # Act
        self.board_page.update_task_name_flow(generated_new_task_name)

        # Assert


if __name__ == '__main__':
    unittest.main()
