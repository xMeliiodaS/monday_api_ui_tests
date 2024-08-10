import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.entites.create_board_payload import CreateBoardPayload
from logic.entites.delete_board_payload import DeleteBoardPayload
from logic.logic_api.create_board import CreateBoard
from logic.logic_api.delete_board import DeleteBoard


class TestCreateBoardAPI(unittest.TestCase):

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
        delete_board_payload = DeleteBoardPayload(self.board_id)
        delete_board = DeleteBoard(self.api_request)
        delete_board.delete_board(delete_board_payload)

    # ------------------------------------------------------------------------

    def test_post_new_board(self):
        """
        Tests the creation of a new board by sending a POST request and verifying the response.

        Checks if the response status code is 200, the response is OK,
         and the response data contains an 'id' for the created board.
        """
        # Arrange
        create_board_payload = CreateBoardPayload()
        create_board = CreateBoard(self.api_request)

        # Act
        response = create_board.post_create_board(create_board_payload)
        self.board_id = response.data['data']['create_board']['id']

        # Assert
        self.assertEqual(response.status, 200, "Expected status code to be 200")
        self.assertTrue(response.ok, "Expected the response to be OK")
        self.assertIn('id', response.data['data']['create_board'], "Expected 'id' in response data")
