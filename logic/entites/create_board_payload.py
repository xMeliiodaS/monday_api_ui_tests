from infra.config_provider import ConfigProvider


class CreateBoardPayload:
    def __init__(self):
        self.config = ConfigProvider.load_config_json()
        self.board_name = self.config['board_name']
        self.board_kind = self.config['board_kind']

    def to_graphql(self):
        """
        Converts the CreateBoardPayload instance to a dictionary representation.

        :return: A dictionary with the GraphQL mutation query for creating a board.
        """
        query = f'mutation {{ create_board (board_name: "{self.board_name}", board_kind: {self.board_kind}) {{ id }} }}'
        return {"query": query}
