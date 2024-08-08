import json

from infra.config_provider import ConfigProvider
from infra.utils import Utils


class DefaultItemPayload:
    def __init__(self):
        """
        Initializes DefaultTaskPayload with the given attributes.
        """
        self.config = ConfigProvider.load_config_json()
        default_task = self.config['create_default_task']

        # From here import from the config file
        self.board_id = self.config['board_id']
        self.group_id = "new_group29179"
        self.pos = default_task['pos']
        self.with_undo_data = self.config['with_undo_data']

        self._name = None
        self.set_name()  # Set the name using the setter method

    @property
    def name(self):
        """
        Gets the name of the task.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the task.
        """
        self._name = value

    def set_name(self):
        """
        Sets the name of the task to a randomly generated key.
        """
        # Set the name to a random key
        self.name = Utils.generate_random_string()

    def to_graphql(self) -> dict:
        """
        Converts the DefaultTaskPayload instance to a GraphQL mutation query.

        :return: A dictionary with the GraphQL mutation query for creating an item.
        """
        column_values = {
            "pos": self.pos,
            "with_undo_data": self.with_undo_data
        }
        column_values_str = json.dumps(column_values).replace('"', '\\"')  # Escape double quotes
        query = (
            f'mutation {{ create_item (board_id: {self.board_id}, '
            f'group_id: "{self.group_id}", item_name: "{self.name}", '
            f'column_values: "{column_values_str}") {{ id }} }}'
        )
        return {"query": query}
