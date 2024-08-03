from infra.config_provider import ConfigProvider


class NewTask:
    ENDPOINT = 'projects'

    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def post_new_default_task(self, user_details):
        url = f"{self.config['url']}{self.ENDPOINT}"
        return self._request.post_request(url, self.config["header"], user_details)
