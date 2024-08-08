from infra.config_provider import ConfigProvider


class CreateBoard:
    """
    Handles operations related to creating a new task in the project management system.
    """

    def __init__(self, request):
        """
        Initializes NewTask with the given request handler and configuration.

        :param request: The request handler to be used for making API calls.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def post_create_board(self, board_payload):
        url = f"{self.config['api_url']}"
        return self._request.post_request(url, self.config["header"], board_payload.to_graphql())
