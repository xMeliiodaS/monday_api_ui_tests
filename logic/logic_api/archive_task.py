from infra.config_provider import ConfigProvider


class ArchiveTask:
    """
    Handles operations related to archiving a new task in the project management system.
    """
    ENDPOINT = 'projects'

    def __init__(self, request):
        """
        Initializes NewTask with the given request handler and configuration.

        :param request: The request handler to be used for making API calls.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def post_archiving_a_task(self, task_payload):
        """
        Sends a POST request to archive a task with the specified payload.

        :param task_payload: The payload with task information to be archived.
        :return: The response from the POST request.
        """
        url = f"{self.config['api_url']}"
        return self._request.post_request(url, self.config["header"], task_payload.to_graphql())

