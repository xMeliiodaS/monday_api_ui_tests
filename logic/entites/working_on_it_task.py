from infra.utils import Utils


class WorkingOnItTask:
    def __init__(self, board_id, column_values, pos, with_undo_data, project_status=None):
        """
        Initializes WorkingOnItTask with the given attributes.

        :param board_id: The ID of the board where the task will be created.
        :param column_values: The values for the columns in the task.
        :param pos: The position of the task on the board.
        :param with_undo_data: A boolean indicating if undo data should be included.
        :param project_status: Optional status information for the project (default is None).
        """
        self.board_id = board_id
        self.group_id = "new_group29179"
        self.column_values = column_values
        self.pos = pos
        self.with_undo_data = with_undo_data
        self.project_status = project_status

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
        self.name = Utils.generate_random_key()

    def to_dict(self):
        """
        Converts the WorkingOnItTask instance to a dictionary representation.

        :return: A dictionary with the task's attributes, including project status if provided.
        """
        payload = {
            "board_id": self.board_id,
            "group_id": self.group_id,
            "name": self.name,
            "column_values": self.column_values,
            "pos": self.pos,
            "with_undo_data": self.with_undo_data
        }
        if self.project_status is not None:
            payload["column_values"]["project_status"] = self.project_status
        return payload
