from infra.config_provider import ConfigProvider


class DeleteBoard:
    """
    Handles operations related to creating a new task in the project management system.
    """
    ENDPOINT = 'projects'

    def __init__(self, request):
        """
        Initializes NewTask with the given request handler and configuration.

        :param request: The request handler to be used for making API calls.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def delete_board(self, delete_board_payload):
        """
        Sends a POST request to delete a board using the provided payload.

        :param delete_board_payload: The payload containing details for the board to be deleted.
        :return: The response from the POST request.
        """
        url = f"{self.config['api_url']}"
        return self._request.post_request(url, self.config["header"], delete_board_payload.to_graphql())
