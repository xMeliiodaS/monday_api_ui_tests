from infra.config_provider import ConfigProvider


class DeleteBoard:
    """
    Handles operations related to creating a new task in the project management system.
    """
    ENDPOINT = 'projects'

    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def delete_board(self, delete_board_payload):
        url = f"{self.config['api_url']}"
        return self._request.post_request(url, self.config["header"], delete_board_payload.to_graphql())
