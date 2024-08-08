import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.entites.default_item_payload import DefaultItemPayload
from logic.logic_api.create_item import CreateItem


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
        pass

    # ------------------------------------------------------------------------

    def test_post_new_default_task(self):
        """
        Tests the creation of a new default task by sending a POST
         request and verifying its appearance on the board.
        """
        # Arrange
        create_task_payload = DefaultItemPayload()
        create_task = CreateItem(self.api_request)

        # Act
        response = create_task.post_create_item(create_task_payload)
        print(response)

        # Assert
        self.assertEqual(response.status, 200, "Expected status code 200 but got {response.status_code}")

        response_data = response.data
        self.assertIn('data', response_data, "Response JSON does not contain 'data'")

        create_item_data = response_data['data'].get('create_item', {})
        self.assertIn('id', create_item_data, "Response JSON does not contain 'id'")
        self.assertIsNotNone(create_item_data['id'], "The 'id' field should not be None")
