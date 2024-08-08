from infra.config_provider import ConfigProvider
from infra.utils import Utils


class WorkingOnItItem:
    def __init__(self):
        """
        Initializes WorkingOnItTask with the given attributes.
        """
        self.config = ConfigProvider.load_config_json()

        self.board_id = self.config['board_id']
        default_task = self.config['create_working_on_it_task']

        self.group_id = "new_group29179"

        self.column_values = {
            "project_status": default_task['column_values']['project_status']
        }
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
        self.name = Utils.generate_random_string()

    def to_dict(self):
        """
        Converts the WorkingOnItTask instance to a dictionary representation.

        :return: A dictionary with the task's attributes, including project status if provided.
        """
        return {
            "board_id": self.board_id,
            "group_id": self.group_id,
            "name": self.name,
            "column_values": self.column_values,
            "pos": self.pos,
            "with_undo_data": self.with_undo_data
        }
