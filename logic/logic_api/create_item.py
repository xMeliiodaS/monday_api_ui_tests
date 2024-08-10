from infra.config_provider import ConfigProvider
from logic.entites.default_item_payload import DefaultItemPayload


class CreateItem:
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

    def post_create_item(self, task_payload):
        """
        Sends a POST request to create a new task with the provided payload.

        :param task_payload: The payload containing task details to be created.
        :return: The response from the POST request.
        """
        url = f"{self.config['api_url']}"
        return self._request.post_request(url, self.config["header"], task_payload.to_graphql())

    def post_create_working_on_it_item(self, task_payload):
        """
        Sends POST requests to create multiple tasks using `DefaultTaskPayload`.

        :param count: The number of tasks to be created.
        """
        url = f"{self.config['url']}{self.ENDPOINT}"
        a = task_payload.to_dict()
        return self._request.post_request(url, self.config["header"], task_payload.to_dict())

    def post_create_multiple_default_items(self, count):
        """
        Sends POST requests to create multiple tasks using `DefaultTaskPayload`.

        :param count: The number of tasks to be created.
        """
        for i in range(count):
            default_task_payload = DefaultItemPayload()
            self.post_create_item(default_task_payload)
