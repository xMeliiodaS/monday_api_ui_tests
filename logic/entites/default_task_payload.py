from infra.config_provider import ConfigProvider
from infra.utils import Utils


class DefaultTaskPayload:
    def __init__(self):
        """
        Initializes DefaultTaskPayload with the given attributes.
        """
        self.config = ConfigProvider.load_config_json()
        default_task = self.config['create_default_task']

        # From here import from the config file
        self.board_id = default_task['board_id']
        self.group_id = "new_group29179"
        self.pos = default_task['pos']
        self.with_undo_data = default_task['with_undo_data']

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

    def to_dict(self):
        """
        Converts the DefaultTaskPayload instance to a dictionary representation.

        :return: A dictionary with the task's attributes.
        """
        return {
            "board_id": self.board_id,
            "group_id": self.group_id,
            "name": self.name,
            "pos": self.pos,
            "with_undo_data": self.with_undo_data
        }
