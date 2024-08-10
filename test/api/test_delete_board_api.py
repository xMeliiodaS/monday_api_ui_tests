import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.entites.create_board_payload import CreateBoardPayload
from logic.entites.delete_board_payload import DeleteBoardPayload
from logic.logic_api.create_board import CreateBoard
from logic.logic_api.delete_board import DeleteBoard


class TestDeleteBoardAPI(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    # ------------------------------------------------------------------------

    def test_delete_board_task(self):
        """
        Tests the deletion of a board by creating a new board and then sending a
         delete request to remove it.

        Checks if the ID in the delete response matches the ID of the board that was created.
        """
        # Arrange
        create_board_payload = CreateBoardPayload()
        create_board = CreateBoard(self.api_request)

        self.board_id = create_board.post_create_board(create_board_payload).data['data']['create_board']['id']

        delete_board_payload = DeleteBoardPayload(self.board_id)
        delete_board = DeleteBoard(self.api_request)

        # Act
        delete_response = delete_board.delete_board(delete_board_payload)

        # Assert
        self.assertEqual(delete_response.data['data']['delete_board']['id'], self.board_id,
                         "The ID in the delete response should match the board ID")
