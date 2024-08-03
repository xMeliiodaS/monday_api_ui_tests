import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.entites.default_task_payload import DefaultTaskPayload
from logic.logic_api.new_task import NewTask


class TestCreateDefaultTask(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    # ------------------------------------------------------------------------

    def test_post_new_default_task(self):

        # Arrange
        default_task_payload = DefaultTaskPayload(self.config['board_id'],
                                                  self.config['column_values'], self.config['pos'],
                                                  self.config['with_undo_data'])
        new_task = NewTask(self.api_request)
        new_task.post_new_default_task(default_task_payload.to_dict())
