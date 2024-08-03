from infra.utils import Utils


class DefaultTaskPayload:
    def __init__(self, board_id, column_values, pos, with_undo_data):
        self.board_id = board_id
        self.group_id = "new_group29179"
        self.column_values = column_values
        self.pos = pos
        self.with_undo_data = with_undo_data

        self._name = None
        self.set_name()  # Set the name using the setter method

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def set_name(self):
        # Set the name to a random key
        self.name = Utils.generate_random_key()

    def to_dict(self):
        return {
            "board_id": self.board_id,
            "group_id": self.group_id,
            "name": self.name,
            "column_values": self.column_values,
            "pos": self.pos,
            "with_undo_data": self.with_undo_data
        }
