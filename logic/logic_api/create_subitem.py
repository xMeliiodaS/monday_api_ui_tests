from infra.config_provider import ConfigProvider
from logic.entites.default_item_payload import DefaultItemPayload


class CreateSubitem:
    def __init__(self, request):
        """
        Initializes NewTask with the given request handler and configuration.

        :param request: The request handler to be used for making API calls.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def post_create_subitem(self, subitem_payload):
        """
        Sends a POST request to create a new subitem using the provided payload.

        :param subitem_payload: The payload containing subitem details to be created.
        :return: The response from the POST request.
        """
        url = f"{self.config['api_url']}"
        return self._request.post_request(url, self.config["header"], subitem_payload.to_graphql())
