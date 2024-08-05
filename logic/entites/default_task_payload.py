from infra.utils import Utils


class DefaultTaskPayload:
    def __init__(self, board_id, column_values, pos, with_undo_data):
        """
        Initializes DefaultTaskPayload with the given attributes.

        :param board_id: The ID of the board where the task will be created.
        :param column_values: The values for the columns in the task.
        :param pos: The position of the task on the board.
        :param with_undo_data: A boolean indicating if undo data should be included.
        """

        # From here import from the config file
        self.board_id = board_id
        self.group_id = "new_group29179"
        self.column_values = column_values
        self.pos = pos
        self.with_undo_data = with_undo_data

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
            "column_values": self.column_values,
            "pos": self.pos,
            "with_undo_data": self.with_undo_data
        }
