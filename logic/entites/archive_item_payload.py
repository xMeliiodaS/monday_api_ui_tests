class ArchiveItemPayload:
    def __init__(self, item_id):
        """
        Initializes ArchiveItemPayload with the given attributes.

        :param item_id: The ID of the item to be archived.
        """
        self.item_id = item_id

    def to_dict(self):
        """
        Converts the ArchiveItemPayload instance to a dictionary representation.

        :return: A dictionary with the GraphQL mutation query for archiving the item.
        """
        query = f'mutation {{ archive_item (item_id: {self.item_id}) {{ id }} }}'
        return {"query": query}
