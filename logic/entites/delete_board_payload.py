class DeleteBoardPayload:
    def __init__(self, board_id: int):
        """
        Initializes the DeleteBoardPayload with the board ID.

        :param board_id: The ID of the board to delete.
        """
        self.board_id = board_id

    def to_graphql(self) -> dict:
        """
        Converts the DeleteBoardPayload instance to a GraphQL mutation query.

        :return: A dictionary with the GraphQL mutation query for deleting a board.
        """
        query = (
            f'mutation {{ delete_board (board_id: {self.board_id}) {{ id }} }}'
        )
        return {"query": query}
