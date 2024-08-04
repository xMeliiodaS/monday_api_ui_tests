from infra.config_provider import ConfigProvider


class NewTask:
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

    def post_create_task(self, task_payload):
        """
        Sends a POST request to create a new task with the provided payload.

        This method can be used to create tasks of various statuses, including
        "Not started," "Working on it," "Stuck," and "Done," based on the details
        included in the payload.

        :param task_payload: The payload containing task details to be created.
        :return: The response from the POST request.
        """
        url = f"{self.config['url']}{self.ENDPOINT}"
        return self._request.post_request(url, self.config["header"], task_payload)
