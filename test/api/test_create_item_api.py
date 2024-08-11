import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.jira_utils import JiraUtils
from logic.entites.default_item_payload import DefaultItemPayload
from logic.entites.delete_item_payload import DeleteItemPayload
from logic.logic_api.create_item import CreateItem
from logic.logic_api.delete_item import DeleteItem


class TestCreateItemAPI(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    # ------------------------------------------------------------------------

    def tearDown(self) -> None:
        """
        Clean up after each test case by deleting all tasks and quitting the WebDriver instance.
        """
        delete_item_payload = DeleteItemPayload(self.item_id)
        delete_item = DeleteItem(self.api_request)
        delete_item.delete_item(delete_item_payload)

    # ------------------------------------------------------------------------

    def test_post_new_default_task(self):
        """
        Tests the creation of a new default task by sending a POST request and verifying the response.

        Checks if the response status code is 200, the response JSON contains
         'data', and the 'id' field in the response is present and not None.
        """
        # Arrange
        create_task_payload = DefaultItemPayload()
        create_task = CreateItem(self.api_request)

        # Act
        response = create_task.post_create_item(create_task_payload)
        self.item_id = response.data['data']['create_item']['id']

        # Assert
        try:
            self.assertEqual(response.status, 201, "Expected status code 200 but got {response.status_code}")
        except AssertionError as e:
            jira_utils = JiraUtils()
            jira_utils.create_issue(self._testMethodName, str(e))
            raise

        response_data = response.data
        self.assertIn('data', response_data, "Response JSON does not contain 'data'")

        create_item_data = response_data['data'].get('create_item', {})
        self.assertIn('id', create_item_data, "Response JSON does not contain 'id'")
        self.assertIsNotNone(create_item_data['id'], "The 'id' field should not be None")
