import json


class ConfigProvider:
    """
    Class for loading configuration from a JSON file.
    """

    @staticmethod
    def load_config_json():
        """
        Load the configuration from the specified JSON file.

        :return: The loaded configuration as a dictionary.
        """
        try:
            # Since we are using with modules with can't use relative path, so changed it to absolute path
            with open(r'D:\Users\User\Desktop\Monday\monday_api_ui_tests\config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")

    @staticmethod
    def load_secret_json():
        """
        Load the configuration from the specified JSON file.

        :return: The loaded configuration as a dictionary.
        """
        try:
            # Since we are using with modules with can't use relative path, so changed it to absolute path
            with open(r'D:\Users\User\Desktop\Steam\Monday_api_ui_tests\secret.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")
