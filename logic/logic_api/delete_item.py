from infra.config_provider import ConfigProvider


class DeleteItem:
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

    def delete_item(self, delete_task_payload):
        """
        Sends a POST request to delete an item using the provided payload.

        :param delete_task_payload: The payload containing details for the item to be deleted.
        :return: The response from the POST request.
        """
        url = f"{self.config['api_url']}"
        return self._request.post_request(url, self.config["header"], delete_task_payload.to_graphql())
