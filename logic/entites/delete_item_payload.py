class DeleteItemPayload:
    def __init__(self, item_id):
        """
        Initializes DeleteItemPayload with the given item ID.

        :param item_id: The ID of the item to be deleted.
        """
        self.item_id = item_id

    def to_graphql(self) -> dict:
        """
        Converts the DeleteItemPayload instance to a GraphQL mutation query.

        :return: A dictionary with the GraphQL mutation query for deleting an item.
        """
        query = (
            f'mutation {{ delete_item (item_id: {self.item_id}) {{ id }} }}'
        )
        return {"query": query}
