from infra.utils import Utils


class DefaultTaskPayload:
    def __init__(self, board_id, column_values, pos, with_undo_data):
        self.board_id = board_id
        self.group_id = "new_group29179"
        self.column_values = column_values
        self.pos = pos
        self.with_undo_data = with_undo_data

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
