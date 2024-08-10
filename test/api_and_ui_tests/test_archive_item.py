import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.entites.archive_item_payload import ArchiveItemPayload
from logic.entites.default_item_payload import DefaultItemPayload
from logic.logic_api.archive_task import ArchiveTask
from logic.logic_api.create_item import CreateItem
from logic.logic_browser.archive_page import ArchivePage
from logic.logic_browser.base_page_app import BasePageApp
from logic.logic_browser.login_page import LoginPage


class TestArchiveItem(unittest.TestCase):
    def setUp(self) -> None:
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

        default_task_payload = DefaultItemPayload()
        self.task_name = default_task_payload.name

        new_task = CreateItem(self.api_request)
        self.task_body = new_task.post_create_item(default_task_payload.to_graphql())

        task_id = self.task_body.data['pulse_data']['id']
        self.archive_task_payload = ArchiveItemPayload(task_id)

    def tearDown(self) -> None:
        # Should add to unarchive and delete item.
        pass

    def test_moving_item_to_archive_exist_there(self):
        """
        Tests the functionality of archiving an item and verifies
         that the item is present in the archive.
        """
        # Act
        archive_task = ArchiveTask(self.api_request)
        archive_task.post_archiving_a_task(self.archive_task_payload.to_graphql())

        base_page = BasePageApp(self.driver)
        base_page.click_on_the_menu_button()
        base_page.click_on_the_archive_button()
        archive_page = ArchivePage(self.driver)

        # Assert
        self.assertTrue(archive_page.is_task_in_archive(self.task_name),
                        "The task is not present in the archive")
