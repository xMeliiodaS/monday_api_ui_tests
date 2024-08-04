from infra.config_provider import ConfigProvider


class NewTask:
    ENDPOINT = 'projects'

    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def post_new_default_task(self, default_task_payload):
        url = f"{self.config['url']}{self.ENDPOINT}"
        return self._request.post_request(url, self.config["header"], default_task_payload)

    def post_new_working_on_it_task(self, working_on_it_task_payload):
        url = f"{self.config['url']}{self.ENDPOINT}"
        return self._request.post_request(url, self.config["header"], working_on_it_task_payload)
