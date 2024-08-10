import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.entites.create_subitem_payload import CreateSubitemPayload
from logic.entites.default_item_payload import DefaultItemPayload
from logic.entites.delete_item_payload import DeleteItemPayload
from logic.logic_api.create_item import CreateItem
from logic.logic_api.create_subitem import CreateSubitem
from logic.logic_api.delete_item import DeleteItem


class TestCreateSubitemAPI(unittest.TestCase):

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
        Tests the creation of a new default task and its associated subitem by
         sending POST requests and verifying the responses.
        """
        # Arrange
        create_task_payload = DefaultItemPayload()
        create_task = CreateItem(self.api_request)

        response = create_task.post_create_item(create_task_payload)
        self.item_id = response.data['data']['create_item']['id']

        create_subitem_payload = CreateSubitemPayload(self.item_id)
        create_subitem = CreateSubitem(self.api_request)

        # Act
        subitem_response = create_subitem.post_create_subitem(create_subitem_payload)
        subitem_id = subitem_response.data['data']['create_subitem']['id']

        # Assert
        self.assertEqual(subitem_response.status, 200,
                         "Subitem creation request failed.")
        self.assertIn('data', subitem_response.data,
                      "Response data does not contain 'data'.")
        self.assertIn('create_subitem', subitem_response.data['data'],
                      "Response data does not contain 'create_subitem'.")
        self.assertEqual(subitem_id, subitem_id,
                         "Subitem ID does not match the expected value.")
