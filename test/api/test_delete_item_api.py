import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.entites.default_item_payload import DefaultItemPayload
from logic.entites.delete_item_payload import DeleteItemPayload
from logic.logic_api.create_item import CreateItem
from logic.logic_api.delete_item import DeleteItem


class TestDeleteItemAPI(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    # ------------------------------------------------------------------------

    def test_delete_new_default_task(self):
        """
        Tests the creation of a new default task by sending a POST
         request and verifying its appearance on the board.
        """
        # Arrange
        create_item_payload = DefaultItemPayload()
        create_item = CreateItem(self.api_request)
        item_id = create_item.post_create_item(create_item_payload).data['data']['create_item']['id']

        delete_item_payload = DeleteItemPayload(item_id)
        delete_item = DeleteItem(self.api_request)

        # Act
        response_delete = delete_item.delete_create_item(delete_item_payload)

        # Assert
        self.assertEqual(response_delete.status, 200,
                         "Expected status code 200 but got {response_delete.status_code}")

        response_delete_data = response_delete.data
        self.assertIn('data', response_delete_data, "Response JSON does not contain 'data'")

        delete_item_data = response_delete_data['data'].get('delete_item', {})
        self.assertIn('id', delete_item_data, "Response JSON does not contain 'id'")
        self.assertEqual(delete_item_data['id'], item_id,
                         "The 'id' field in the delete response does not match the created item ID")
