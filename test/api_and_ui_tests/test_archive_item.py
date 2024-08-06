import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.entites.archive_item_payload import ArchiveItemPayload
from logic.entites.default_task_payload import DefaultTaskPayload
from logic.logic_api.archive_task import ArchiveTask
from logic.logic_api.new_tasks import NewTask
from logic.logic_browser.home_page import HomePage
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

        default_task_payload = DefaultTaskPayload()
        new_task = NewTask(self.api_request)

        self.task_body = new_task.post_create_task(default_task_payload.to_dict())

    def test_moving_item_to_archive(self):
        task_id = self.task_body.data['pulse_data']['id']
        archive_task_payload = ArchiveItemPayload(task_id)

        archive_task = ArchiveTask(self.api_request)
        archive_task.post_archiving_a_task(archive_task_payload.to_dict())
